from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()
@app.get("/web")
def web():
    return FileResponse("index.html")
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
        model="gpt-5.4-mini",
        input=req.question
    )

    return {
        "answer": response.output_text
    }
