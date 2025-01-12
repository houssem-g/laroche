# app/services/chatgpt.py

import openai
from app.config import settings, logger


class ChatGPTClient:
    def __init__(self, api_key: str = settings.OPENAI_API_KEY):
        openai.api_key = api_key
        self.logger = logger

    def generate_response(self, prompt: str) -> str:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Please respond in English."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            message = response.choices[0].message
            self.logger.info(f"ChatGPT response: {message}")
            return message
        except Exception as e:
            self.logger.error(f"ChatGPT Error: {e}")
            return "Désolé, je ne peux pas traiter votre demande pour le moment."
