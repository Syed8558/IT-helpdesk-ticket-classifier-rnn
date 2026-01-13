🧠 IT Helpdesk Ticket Classification using RNN

This project implements a Recurrent Neural Network (RNN) to automatically classify IT helpdesk support tickets based on their textual descriptions.
It simulates a real-world enterprise IT support system where incoming tickets are automatically routed to the correct support team.

📌 Business Problem

Large IT teams receive thousands of support tickets every day.
Manually reading and assigning tickets causes:

Delays

SLA violations

Increased workload

This system predicts the issue category of a ticket so it can be routed instantly.

Example categories:

Hardware Issue

Software Issue

Network Problem

Password Reset

Access Request

System Error

Security Incident

🚀 Solution

We use an RNN-based deep learning model trained on historical ticket descriptions to predict the category of a new ticket automatically.

The system:

Extracts text from PDF and JSON tickets

Builds a training dataset

Trains an RNN text classifier

Exposes predictions through an API

🧠 Machine Learning Pipeline
PDF / JSON Tickets
        ↓
Text Extraction
        ↓
Text Cleaning & Tokenization
        ↓
RNN Model Training
        ↓
Model Evaluation
        ↓
Prediction API

📁 Project Structure
it-helpdesk-ticket-classifier-rnn/
│
├── src/
│   ├── build_dataset.py     # Extracts text from PDF & JSON files
│   ├── preprocess.py       # Text cleaning & tokenization
│   ├── model.py            # RNN architecture
│   ├── train.py            # Model training
│   └── evaluate.py         # Performance evaluation
│
├── api/
│   └── app.py              # REST API for predictions
│
├── data/
│   ├── .gitkeep
│   └── README.md           # Dataset instructions
│
├── models/                 # Trained models (not committed)
├── requirements.txt
├── .gitignore
└── README.md

📊 Dataset

The project uses IT helpdesk ticket data in PDF and JSON format.

Due to privacy and size constraints, the dataset is not included in this repository.
Place your dataset files inside the data/ folder before running the project.

⚙️ Installation
pip install -r requirements.txt

▶️ Build Dataset

Extract text from tickets and create training data:

python src/build_dataset.py

▶️ Train the RNN Model
python src/train.py

🌐 Run the Prediction API
python api/app.py


API runs at:

http://127.0.0.1:8000

🔮 Sample API Request
{
  "ticket_text": "User is unable to connect to WiFi network in office"
}


Response:

{
  "predicted_category": "Network_Problem"
}

🛠 Tech Stack

Python

TensorFlow (RNN)

Pandas, NumPy

NLTK, spaCy

PyPDF2

Flask / FastAPI

💼 Why This Project Matters

This project demonstrates:

Natural Language Processing

Deep Learning with RNN

Data extraction from real documents

End-to-end ML pipeline

Production-style API deployment

This is a real enterprise use case, not a toy example.

👨‍💻 Author

Syed Sadath G
Data Scientist | NLP | Deep Learning




