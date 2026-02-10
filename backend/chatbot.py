from langdetect import detect
from deep_translator import GoogleTranslator

def translate_to_en(text):
    return GoogleTranslator(source='auto', target='en').translate(text)

def translate_back(text, lang):
    return GoogleTranslator(source='en', target=lang).translate(text)

def chatbot_reply(message):

    lang = detect(message)
    text = translate_to_en(message).lower()

    if "yellow" in text:
        response = "Possible nitrogen deficiency. Use balanced fertilizer."

    elif "spots" in text:
        response = "Possible fungal infection. Spray fungicide."

    elif "watering" in text:
        response = "Water early morning to avoid leaf diseases."

    else:
        response = "Upload plant image for disease detection."

    return translate_back(response, lang)
