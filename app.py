from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/chat")
async def chat(req: ChatRequest):

    response = client.responses.create(
        model="gpt-5.5-mini",
        input=req.question
    )

    return {
        "answer": response.output_text
    }
