# src/flow/prompt_block.py
import aiohttp
import json
import logging
import re
import csv
import io
from fpdf import FPDF
from typing import Optional, Dict, Any, List, Tuple

from src.utils.exceptions import APIException
from src.api.model_api import ExternalData, WebData, APIData, TXTData, CSVData

class OutputSaver:
    @staticmethod
    def save_txt(content: str, filename: str):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def save_pdf(content: str, filename: str):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, content)
        pdf.output(filename)

class PromptBlock:
    def __init__(self, prompt: str, model: str = "gpt-3.5-turbo", max_tokens: int = 2000, 
                 temperature: float = 0.7, external_data: Optional[ExternalData] = None,
                 semantic_search: Optional[Dict[str, Any]] = None, 
                 save_output: Optional[Dict[str, str]] = None):
        self.prompt = prompt
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.output = None
        self.input_blocks: List[Tuple[int, int]] = []
        self.external_data = external_data
        self.semantic_search = semantic_search
        self.save_output = save_output

    def add_input(self, step_index: int, block_index: int):
        self.input_blocks.append((step_index, block_index))

    async def load_external_data(self, session: aiohttp.ClientSession) -> str:
        if not self.external_data:
            return ""
        try:
            return await self.external_data.load_data(session)
        except Exception as e:
            logging.error(f"Erreur lors du chargement des données externes depuis {self.external_data.source}: {str(e)}")
            return f"Erreur lors du chargement des données externes: {str(e)}"

    def save_block_output(self):
        if self.save_output and self.output:
            output_format = self.save_output.get('format', 'txt').lower()
            filename = self.save_output.get('filename', f'output_{id(self)}.{output_format}')
            
            try:
                if output_format == 'txt':
                    OutputSaver.save_txt(self.output, filename)
                elif output_format == 'pdf':
                    OutputSaver.save_pdf(self.output, filename)
                else:
                    raise ValueError(f"Format de sortie non supporté : {output_format}")
                print(f"Sortie sauvegardée dans {filename}")
            except Exception as e:
                logging.error(f"Erreur lors de la sauvegarde de la sortie : {str(e)}")
