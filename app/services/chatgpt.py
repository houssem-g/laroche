# app/services/chatgpt.py

import openai
from app.config import settings

class ChatGPTClient:
    def __init__(self, api_key: str = settings.OPENAI_API_KEY):
        openai.api_key = api_key

    def generate_response(self, prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"ChatGPT Error: {e}")
            return "Désolé, je ne peux pas traiter votre demande pour le moment."
