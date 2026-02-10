from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import shutil
from advisory import get_advisory
from chatbot import chatbot_reply
from gradcam import generate_gradcam
from voice_input import speech_to_text
from tts import speak_hindi

app = FastAPI()

model = YOLO("backend/model/best.pt")

# -----------------------------------
# Disease detection
# -----------------------------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    path = "temp.jpg"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = model.predict(path)

    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls)
            name = model.names[cls]
            conf = float(box.conf)

            detections.append({
                "disease": name,
                "confidence": conf,
                "advisory": get_advisory(name)
            })

    return {"detections": detections}


# -----------------------------------
# GradCAM
# -----------------------------------
@app.post("/gradcam")
async def gradcam(file: UploadFile = File(...)):
    path = "temp.jpg"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    heatmap = generate_gradcam(model, path)

    return {"heatmap": heatmap}


# -----------------------------------
# Chatbot
# -----------------------------------
@app.post("/chatbot")
async def chatbot(message: str):
    reply = chatbot_reply(message)
    return {"reply": reply}


# -----------------------------------
# Voice assistant
# -----------------------------------
@app.post("/voice-assistant")
async def voice_assistant(file: UploadFile = File(...)):

    audio_path = "voice.wav"
    with open(audio_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = speech_to_text(audio_path)
    reply = chatbot_reply(text)
    audio = speak_hindi(reply)

    return {"text": reply, "audio": audio}
