from fastapi import FastAPI
from app.service.llm_service import LLMService

client = LLMService()

app = FastAPI(
    title="Orbit AI Assistant",
    version="1.0.0"
)

@app.get("/embed")
async def embed_content(content: str):
    embedding = client.embed_content(content)
    return {"embedding": embedding}


@app.post("/chat")
async def chat(messages: list[dict]):
    response = client.generate_content(messages)
    return {"response": response}