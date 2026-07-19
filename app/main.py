from fastapi import FastAPI
from app.service.llm_service import LLMService

client = LLMService()

app = FastAPI(
    title="Orbit AI Assistant",
    version="1.0.0"
)

@app.middleware("http")
async def debug_path(request, call_next):
    print("PATH:", request.url.path)
    response = await call_next(request)
    return response

@app.get("/")
async def root():
    return {"message": "Welcome to the Orbit AI Assistant API!"}

@app.get("/embed")
async def embed_content(content: str):
    embedding = client.embed_content(content)
    return {"embedding": embedding}


@app.post("/chat")
async def chat(messages: list[dict]):
    response = client.generate_content(messages)
    return {"response": response}