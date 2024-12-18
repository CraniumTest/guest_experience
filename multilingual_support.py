from googletrans import Translator

def translate_message(message, target_language):
    translator = Translator()
    translation = translator.translate(message, dest=target_language)
    return translation.text
