from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/web")
def web():
    return FileResponse("index.html")

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(req: ChatRequest):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=req.question
    )

    return {
        "answer": response.output_text
    }
