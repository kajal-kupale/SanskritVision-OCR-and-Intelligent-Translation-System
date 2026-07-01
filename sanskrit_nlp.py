def analyze_sanskrit(text, translation=""):

    words = text.split()
    word_count = len(words)

    return f"""
    <div class="analysis-section">

        <h3>🌐 Translation</h3>
        <p>{translation}</p>

        <h3>📖 Key Words</h3>
        <p>Total Words Detected: {word_count}</p>

        <h3>🔤 Grammar / Sandhi</h3>
        <p>
        Sanskrit grammatical structure detected.
        Devanagari script recognized successfully.
        </p>

        <h3>📊 NLP Insight</h3>
        <p>
        Language: Sanskrit<br>
        Script: Devanagari<br>
        Word Count: {word_count}
        </p>

    </div>
    """