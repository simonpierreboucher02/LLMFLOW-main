# src/api/api_client.py
import aiohttp
import logging
from typing import List, Dict, Any

from .model_api import OpenAIAPI, AnthropicAPI, MistralAPI
from src.utils.token_utils import num_tokens_from_string
from src.utils.exceptions import APIException

class APIClient:
    def __init__(self, api_keys: Dict[str, str]):
        self.apis = {
            "openai": OpenAIAPI(api_keys.get("openai")),
            "anthropic": AnthropicAPI(api_keys.get("anthropic")),
            "mistral": MistralAPI(api_keys.get("mistral")),
        }

    async def generate_text(self, session: aiohttp.ClientSession, model: str, prompt: str, 
                            temperature: float, max_tokens: int) -> str:
        if model.startswith(("gpt", "text-davinci")):
            api_type = "openai"
        elif model.startswith("claude"):
            api_type = "anthropic"
        elif model.startswith("mistral"):
            api_type = "mistral"
        else:
            raise ValueError(f"Unsupported model: {model}")
        
        try:
            token_limit = 16000  # Ajuster en fonction du modèle
            if num_tokens_from_string(prompt, model) > token_limit:
                logging.info(f"Prompt dépasse la limite de tokens. Division en plusieurs parties.")
                return await self.split_and_process(session, model, prompt, temperature, max_tokens, token_limit)
            else:
                response = await self.apis[api_type].generate_text(session, model, prompt, temperature, max_tokens)
                return self.apis[api_type].extract_text_from_response(response)
        except APIException as e:
            logging.error(f"Erreur API: {str(e)}")
            return "Erreur : Impossible de générer le texte."

    async def split_and_process(self, session: aiohttp.ClientSession, model: str, prompt: str, 
                                temperature: float, max_tokens: int, token_limit: int) -> str:
        parts = self.split_prompt(prompt, token_limit)
        responses = []

        for i, part in enumerate(parts):
            logging.info(f"Traitement de la partie {i+1} sur {len(parts)}")
            response = await self.generate_text(session, model, part, temperature, max_tokens // len(parts))
            responses.append(response)
            logging.info(f"Partie {i+1} traitée")

        response_combinee = " ".join(responses)
        logging.info("Toutes les parties traitées. Combinaison des réponses.")

        if num_tokens_from_string(response_combinee, model) > token_limit:
            logging.info("Réponse combinée dépasse la limite de tokens. Génération d'un résumé.")
            summary_prompt = f"Résumé du texte suivant :\n\n{response_combinee}"
            final_response = await self.generate_text(session, model, summary_prompt, temperature, max_tokens)
            logging.info("Résumé généré.")
            return final_response
        else:
            logging.info("Retour de la réponse combinée.")
            return response_combinee

    def split_prompt(self, prompt: str, token_limit: int) -> List[str]:
        words = prompt.split()
        parts = []
        current_part = []
        current_tokens = 0

        for word in words:
            word_tokens = num_tokens_from_string(word, "gpt-3.5-turbo")
            if current_tokens + word_tokens > token_limit:
                if current_part:
                    parts.append(" ".join(current_part))
                current_part = [word]
                current_tokens = word_tokens
            else:
                current_part.append(word)
                current_tokens += word_tokens

        if current_part:
            parts.append(" ".join(current_part))

        return parts

    async def get_embeddings(self, session: aiohttp.ClientSession, texts: List[str]) -> List[List[float]]:
        return await self.apis["openai"].get_embeddings(session, texts)
