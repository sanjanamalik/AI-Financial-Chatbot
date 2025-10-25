from fastapi import FastAPI
from backend.chatbot_logic import get_financial_response


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Financial Chatbot API is running successfully!"}

@app.get("/ask/")
def ask_bot(query: str):
    response = get_financial_response(query)
    return {"response": response}
