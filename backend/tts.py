from gtts import gTTS

def speak_hindi(text):
    tts = gTTS(text=text, lang='hi')
    file = "response.mp3"
    tts.save(file)
    return file
