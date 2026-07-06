import os
import json
import time

from google import genai


class AIClient:

    def __init__(self):

        # ---------------------------------------------
        # STREAMLIT CLOUD
        # ---------------------------------------------
        try:
            import streamlit as st

            if "GEMINI_API_KEY" in st.secrets:
                api_key = st.secrets["GEMINI_API_KEY"]
            else:
                raise Exception()

        # ---------------------------------------------
        # LOCAL (.env)
        # ---------------------------------------------
        except Exception:

            from dotenv import load_dotenv

            load_dotenv()

            api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY não encontrada no .env nem no Streamlit Secrets."
            )

        self.client = genai.Client(api_key=api_key)

        # Modelo padrão
        self.model = "gemini-2.5-flash-lite"

    def generate(self, prompt: str, retries: int = 3):

        last_error = None

        for attempt in range(retries):

            try:

                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )

                text = response.text.strip()

                # Remove markdown caso exista
                if text.startswith("```"):
                    text = (
                        text.replace("```json", "")
                            .replace("```", "")
                            .strip()
                    )

                return json.loads(text)

            except json.JSONDecodeError:

                last_error = ValueError(
                    f"O Gemini não retornou JSON válido:\n\n{text}"
                )

            except Exception as e:

                last_error = e

                # Retry apenas em erros temporários
                error_text = str(e)

                if (
                    "429" in error_text
                    or "503" in error_text
                    or "RESOURCE_EXHAUSTED" in error_text
                    or "UNAVAILABLE" in error_text
                ):

                    wait = 2 ** attempt
                    print(f"Retry {attempt+1}/{retries} em {wait}s...")
                    time.sleep(wait)
                    continue

                break

        raise RuntimeError(f"Falha ao chamar o Gemini:\n{last_error}")