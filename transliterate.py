from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def transliterate_text(sanskrit_text):
    return transliterate(sanskrit_text, sanscript.DEVANAGARI, sanscript.ITRANS)
