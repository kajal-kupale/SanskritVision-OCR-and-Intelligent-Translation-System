from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# ---------------- USER ----------------
class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)

    # Relationship with TranslationHistory
    history = db.relationship(
        'TranslationHistory',
        backref='user',
        lazy=True
    )


# ---------------- TRANSLATION HISTORY ----------------
class TranslationHistory(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    input_text = db.Column(db.Text, nullable=False)

    translated_text = db.Column(db.Text)

    source = db.Column(db.String(20))

    target_lang = db.Column(db.String(10))

    timestamp = db.Column(db.DateTime, default=datetime.now
    )
    