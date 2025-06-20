# run.py
import asyncio
import logging
import os

from dotenv import load_dotenv
from src.utils.config import load_steps_config, create_modular_flow

# Charger les variables d'environnement
load_dotenv()

# Configurer le logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Récupérer les clés API depuis les variables d'environnement
    api_keys = {
        "openai": os.getenv("OPENAI_API_KEY"),
        "anthropic": os.getenv("ANTHROPIC_API_KEY"),
        "mistral": os.getenv("MISTRAL_API_KEY")
    }

    # Charger la configuration des étapes depuis le fichier config.json
    steps_config = load_steps_config("config.json")

    # Créer le FlowManager avec la configuration des étapes
    flow_manager = create_modular_flow(steps_config, api_keys)

    # Exécuter le flux
    asyncio.run(flow_manager.run_flow())

if __name__ == "__main__":
    main()
