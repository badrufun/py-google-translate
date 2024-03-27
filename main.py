from googletrans import Translator


def translate_text(text, target_language='en'):
    translator = Translator()
    traslated_text = translator.translate(text, dest=target_language)
    return traslated_text.text


if __name__ == '__main__':
    text_to_translate = "Bonjour tout le monde"
    translated_text = translate_text(text_to_translate, target_language='hi')
    print("Translated text:", translated_text)

