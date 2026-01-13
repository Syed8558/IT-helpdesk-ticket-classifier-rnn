from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import joblib
import numpy as np

# Load model and tokenizer
model = tf.keras.models.load_model("models/rnn_model")
tokenizer = joblib.load("models/tokenizer.pkl")

MAX_LEN = 200

app = FastAPI(title="IT Helpdesk Ticket Classifier")

class Ticket(BaseModel):
    ticket_text: str

labels = [
    "Hardware_Issue",
    "Software_Issue",
    "Network_Problem",
    "Password_Reset",
    "Access_Request",
    "System_Error",
    "Security_Incident"
]

@app.post("/predict")
def predict(ticket: Ticket):
    seq = tokenizer.texts_to_sequences([ticket.ticket_text])
    padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=MAX_LEN)

    pred = model.predict(padded)
    class_id = int(np.argmax(pred))
    confidence = float(np.max(pred))

    return {
        "predicted_category": labels[class_id],
        "confidence": round(confidence, 3)
    }

