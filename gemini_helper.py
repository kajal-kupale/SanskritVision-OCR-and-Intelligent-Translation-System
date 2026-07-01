import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("models/gemini-2.5-flash")


def explain_sanskrit(text):

    prompt = f"""
You are an expert in Sanskrit language and literature.

Analyze the Sanskrit text below.

Return ONLY HTML.

Do NOT return Markdown.

Do NOT repeat the translated text.

Generate ONLY the following three sections.

<h3> 🌟 Key Words</h3>
<ul>
<li> 3 important keywords separated by commas.</li>
</ul>

<br><br>

<h3> 🧠 Sentiment Analysis</h3>
<p>
Mention whether the text is Positive, or  Negative.  

</p>

<br><br>

<h3> 🔍 AI  Insight</h3>
<p>
Explain the overall meaning and significance of the Sanskrit verse in only 1 to 2 very small concise sentences.
Do not repeat the translation.
</p>

Sanskrit Text:

{text}
"""

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"""
<h3>❌ AI Error</h3>
<p>{e}</p>
"""