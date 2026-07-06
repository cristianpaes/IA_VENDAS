import os
import json
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()


class AIClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY não encontrada")

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.5-flash-lite"

    def generate(self, prompt: str, retries: int = 3):

        last_error = None

        for i in range(retries):

            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )

                text = response.text
                text = text.replace("```json", "").replace("```", "").strip()

                return json.loads(text)

            except Exception as e:

                last_error = e
                wait = 2 ** i  # backoff exponencial
                time.sleep(wait)

        raise RuntimeError(f"Falha no Gemini após retries: {last_error}")