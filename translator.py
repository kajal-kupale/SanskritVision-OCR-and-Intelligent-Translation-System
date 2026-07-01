from deep_translator import GoogleTranslator

def translate_text(text, lang):
    try:
        return GoogleTranslator(
            source="auto",
            target=lang.lower()      # ← Add .lower()
        ).translate(text)

    except Exception as e:
        print("\n========== TRANSLATION ERROR ==========")
        print(e)
        print("=======================================\n")
        return f"ERROR: {e}"