from googletrans import Translator

def translate_text(text, src_lang='auto', dest_lang='en'):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    text = input("Enter text to translate: ")
    src_lang = input("Enter source language code : ") or 'auto'
    dest_lang = input("Enter target language code : ") or 'en'

    translated_text = translate_text(text, src_lang, dest_lang)
    print(f"Translated text: {translated_text}")