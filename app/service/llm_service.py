from google import genai
from app.repositories.message_repository import MessageRepository
from app.config import GEMINI_API_KEY
from app.models.messages import Message

client = genai.Client(api_key=GEMINI_API_KEY)
message_repository = MessageRepository()
class LLMService:
    def __init__(self):
        self.client = client

    def embed_content(self, content: str):
        messages = message_repository.get_all()
        for message in messages:
            text = f"{message.subject}\n{message.body}"
            result = self.client.models.embed_content(
                model="gemini-embedding-2",
                contents=text
            )
            message.embedding = result.embeddings[0].values
            message_repository.update(message)

    def generate_content(self, prompt: str):
        result = self.client.models.embed_content(
                model="gemini-embedding-2",
                contents=prompt[-1]["content"]
        )
        embedding = result.embeddings[0].values
        
        messages = message_repository.search_similar(embedding, limit=5)
        context = "\n".join([f"Subject: {m.subject}\nBody: {m.body}" for m in messages])
        prompt = f"Context:\n{context}\n\nUser Prompt:\n{prompt}"

        result = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return result.candidates[0].content.parts[0].text