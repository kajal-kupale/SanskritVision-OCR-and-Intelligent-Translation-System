import os, re
from datetime import datetime
from flask import (
    Flask, render_template, request,
    redirect, url_for, send_file, flash
)
from flask_login import (
    LoginManager, login_user, login_required,
    logout_user, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from models import db, User, TranslationHistory
from ocr import extract_text
from translator import translate_text
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from gemini_helper import explain_sanskrit
from sanskrit_nlp import analyze_sanskrit

# ---------------- APP CONFIG ----------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'final-academic-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql2345@localhost/sanskritocr'
app.config['UPLOAD_FOLDER'] = 'uploads'
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# ---------- SANSKRIT CHECK ----------
def looks_like_sanskrit(text):
    if not text:
        return False
    return len(re.findall(r'[\u0900-\u097F]', text)) >= 10



#---------forgot password------
@app.route('/forgot-password')
def forgot_password():
    return "<h2>Forgot Password feature will be available soon.</h2>"

# ---------- HOME ----------
@app.route('/')
def home():

    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    return redirect(url_for('login'))


# ---------- LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password", "error")

    return render_template('login.html')


# ---------- REGISTER ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        if User.query.filter_by(email=request.form['email']).first():
            flash("Email already registered", "error")
            return redirect(url_for('register'))

        db.session.add(User(
            username=request.form['username'],
            email=request.form['email'],
            password=generate_password_hash(request.form['password'])
        ))
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/dashboard')
@login_required
def dashboard():

    total = TranslationHistory.query.filter_by(
        user_id=current_user.id
    ).count()

    image_total = TranslationHistory.query.filter_by(
        user_id=current_user.id,
        source="Image"
    ).count()

    paste_total = TranslationHistory.query.filter_by(
        user_id=current_user.id,
        source="Text"
    ).count()

    return render_template(
        "dashboard.html",
        total=total,
        image_total=image_total,
        paste_total=paste_total,
        user=current_user
    )


# ---------- OCR UPLOAD ----------
@app.route('/ocr', methods=['GET', 'POST'])
@login_required
def ocr_page():

    text = result = warning = ai_explanation = ""
    confidence = 0
    success = False

    if request.method == 'POST':

        img = request.files.get('image')
        target = request.form.get('target_lang', 'en')

        if img and img.filename:

            path = os.path.join(
                app.config['UPLOAD_FOLDER'],
                secure_filename(img.filename)
            )

            img.save(path)

            text, confidence = extract_text(path)

            if looks_like_sanskrit(text):

                result = translate_text(text, target)

                try:

                    ai_explanation = explain_sanskrit(text)

                    if (
                        "quota" in ai_explanation.lower()
                        or "429" in ai_explanation
                        or "rate limit" in ai_explanation.lower()
                    ):
                        ai_explanation = analyze_sanskrit(
                            text,
                            result
                        )

                except:

                    ai_explanation = analyze_sanskrit(
                        text,
                        result
                    )

                success = True

                db.session.add(
                    TranslationHistory(
                        user_id=current_user.id,
                        input_text=text,
                        translated_text=result,
                        source="Image",
                        target_lang=target
                    )
                )

                db.session.commit()

            else:
                warning = "Unable to detect valid Sanskrit text."

    return render_template(
        'ocr.html',
        text=text,
        result=result,
        ai_explanation=ai_explanation,
        success=success,
        warning=warning
    )

# ---------- PASTE TEXT ----------
@app.route('/paste', methods=['GET', 'POST'])
@login_required
def paste_page():

    text = result = warning = ai_explanation = ""
    success = False

    if request.method == 'POST':

        text = request.form.get('sanskrit_text')
        target = request.form.get('target_lang', 'en')

        if looks_like_sanskrit(text):

            result = translate_text(text, target)

            try:

                ai_explanation = explain_sanskrit(text)

                if (
                    "quota" in ai_explanation.lower()
                    or "429" in ai_explanation
                    or "rate limit" in ai_explanation.lower()
                ):
                    ai_explanation = analyze_sanskrit(
                        text,
                        result
                    )

            except:

                ai_explanation = analyze_sanskrit(
                    text,
                    result
                )

            success = True

            db.session.add(
                TranslationHistory(
                    user_id=current_user.id,
                    input_text=text,
                    translated_text=result,
                    source="Text",
                    target_lang=target
                )
            )

            db.session.commit()

        else:
            warning = "Invalid Sanskrit text."

    return render_template(
        'paste.html',
        text=text,
        result=result,
        ai_explanation=ai_explanation,
        success=success,
        warning=warning
    )




# ---------- HISTORY ----------
@app.route('/history')
@login_required
def history_page():

    history = TranslationHistory.query.filter_by(
        user_id=current_user.id
    ).order_by(
        TranslationHistory.timestamp.desc()
    ).all()

    total = len(history)

    return render_template(
        'history.html',
        history=history,
        total=total,
        user=current_user
    )



#--------profile--------
@app.route('/profile')
@login_required
def profile():

    total = TranslationHistory.query.filter_by(
        user_id=current_user.id
    ).count()

    image_count = TranslationHistory.query.filter_by(
        user_id=current_user.id,
        source="Image"
    ).count()

    text_count = TranslationHistory.query.filter_by(
        user_id=current_user.id,
        source="Text"
    ).count()

    return render_template(
        "profile.html",
        total=total,
        image_count=image_count,
        text_count=text_count
    )
@app.route("/analysis")
@login_required
def analysis():

    records = TranslationHistory.query.filter_by(
        user_id=current_user.id
    ).all()

    total = len(records)

    image_count = sum(1 for r in records if r.source == "Image")
    text_count = sum(1 for r in records if r.source == "Text")

    lang_data = {}

    for row in records:
        lang = row.target_lang.upper()
        lang_data[lang] = lang_data.get(lang, 0) + 1

    return render_template(
        "analysis.html",
        total=total,
        image_count=image_count,
        text_count=text_count,
        lang_labels=list(lang_data.keys()),
        lang_counts=list(lang_data.values()),
        time_now=datetime.now().strftime("%d %B %Y, %H:%M")
    )
# ----------  PDF ----------
@app.route('/analysis/download')
@login_required
def download_analysis():

    pdf_path = "static/analysis.pdf"

    doc = SimpleDocTemplate(pdf_path, pagesize=A4)

    styles = getSampleStyleSheet()

    total = TranslationHistory.query.filter_by(
        user_id=current_user.id
    ).count()

    image_count = TranslationHistory.query.filter_by(
        user_id=current_user.id,
        source="Image"
    ).count()

    text_count = TranslationHistory.query.filter_by(
        user_id=current_user.id,
        source="Text"
    ).count()

    story = []

    # ---------------- Title ----------------

    story.append(
        Paragraph(
            "Sanskrit OCR & AI Translation System",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    # ---------------- User ----------------

    story.append(
        Paragraph(
            "<b>User Information</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Username : {current_user.username}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Email : {current_user.email}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Generated On : {datetime.now().strftime('%d %B %Y, %H:%M')}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,18))

    # ---------------- Statistics ----------------

    story.append(
        Paragraph(
            "<b>Translation Statistics</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Total Translations : {total}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"OCR Uploads : {image_total}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Paste Text : {paste_total}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,18))

    # ---------------- Features ----------------

    story.append(
        Paragraph(
            "<b>System Features</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "• Sanskrit OCR from Images",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "• Multi-language Translation",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "• AI Sanskrit Explanation",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "• Translation History",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "• Usage Analysis Dashboard",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    # ---------------- Footer ----------------

    story.append(
        Paragraph(
            "<b>Academic Project (2026)</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            "Generated by Sanskrit OCR & AI Translation System",
            styles["Normal"]
        )
    )

    doc.build(story)

    return send_file(pdf_path, as_attachment=True)
# ---------- LOGOUT ----------
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "success")
    return redirect(url_for('dashboard'))


# ---------- RUN ----------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)