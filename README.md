# LLM Flow Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![GitHub Issues](https://img.shields.io/github/issues/simonpierreboucher02/LLMFLOW-main)](https://github.com/simonpierreboucher02/LLMFLOW-main/issues)
[![GitHub Forks](https://img.shields.io/github/forks/simonpierreboucher02/LLMFLOW-main)](https://github.com/simonpierreboucher02/LLMFLOW-main/network)
[![GitHub Stars](https://img.shields.io/github/stars/simonpierreboucher02/LLMFLOW-main)](https://github.com/simonpierreboucher02/LLMFLOW-main/stargazers)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/simonpierreboucher02/LLMFLOW-main)](https://github.com/simonpierreboucher02/LLMFLOW-main/commits/main)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/simonpierreboucher02/LLMFLOW-main)](https://github.com/simonpierreboucher02/LLMFLOW-main)
[![GitHub Language](https://img.shields.io/github/languages/top/simonpierreboucher02/LLMFLOW-main)](https://github.com/simonpierreboucher02/LLMFLOW-main)
[![GitHub Contributors](https://img.shields.io/github/contributors/simonpierreboucher02/LLMFLOW-main)](https://github.com/simonpierreboucher02/LLMFLOW-main/graphs/contributors)

[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4%20%7C%20GPT--3.5-orange?logo=openai)](https://openai.com/)
[![Anthropic](https://img.shields.io/badge/Anthropic-Claude-blue?logo=anthropic)](https://anthropic.com/)
[![Mistral](https://img.shields.io/badge/Mistral-Mistral%20AI-purple?logo=mistral)](https://mistral.ai/)
[![AsyncIO](https://img.shields.io/badge/AsyncIO-Asynchronous%20Processing-green?logo=python)](https://docs.python.org/3/library/asyncio.html)
[![Graphviz](https://img.shields.io/badge/Graphviz-Flow%20Visualization-red?logo=graphviz)](https://graphviz.org/)

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?logo=python)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

<div align="center">
  <img src="https://img.shields.io/badge/LLM%20Flow%20Framework-🚀%20AI%20Workflow%20Orchestration-brightgreen?style=for-the-badge&logo=python" alt="LLM Flow Framework">
</div>

## 📊 Repository Metrics

| Metric | Value |
|--------|-------|
| **Lines of Code** | ~500+ |
| **Python Files** | 12 |
| **Dependencies** | 10 |
| **Supported LLM APIs** | 3 (OpenAI, Anthropic, Mistral) |
| **Output Formats** | TXT, PDF |
| **Async Processing** | ✅ |
| **Flow Visualization** | ✅ |
| **Semantic Search** | ✅ |

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
  - [Flow Configuration](#flow-configuration)
- [Usage](#usage)
  - [Running the Flow](#running-the-flow)
- [Project Structure](#project-structure)
- [Example Use Case](#example-use-case)
- [Extending the Framework](#extending-the-framework)
- [Contribution](#contribution)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

The **LLM Flow Framework** is a modular and extensible Python-based system designed to orchestrate complex workflows involving Large Language Models (LLMs) such as OpenAI's GPT, Anthropic's Claude, and Mistral's models. This framework allows users to define, configure, and execute multi-step prompt flows, enabling sophisticated text generation, data processing, and integration with external data sources.

Whether you're building a multiple-choice question generator, a content summarizer, or any other LLM-driven application, the LLM Flow Framework provides the flexibility and scalability to meet your needs.

### 🎯 Key Benefits

- **⚡ Asynchronous Processing**: High-performance, non-blocking API calls
- **🔗 Multi-API Support**: Seamless integration with leading LLM providers
- **🌐 External Data Integration**: Load data from web sources, APIs, and local files
- **🔍 Semantic Search**: Enhanced prompt relevance and response quality
- **📊 Flow Visualization**: Visual workflow representation with Graphviz
- **⚙️ JSON Configuration**: Easy workflow definition and customization

## Features

- **Asynchronous Processing**: Leverages `asyncio` and `aiohttp` for efficient, non-blocking API calls.
- **Multi-API Support**: Integrates with OpenAI, Anthropic, and Mistral APIs for diverse language model capabilities.
- **External Data Integration**: Supports loading data from web sources, APIs, and local files (TXT, CSV).
- **Semantic Search**: Implements semantic search to enhance prompt relevance and response quality.
- **Flexible Output Saving**: Saves generated outputs in various formats, including TXT and PDF.
- **Flow Visualization**: Uses Graphviz to visualize the workflow, making it easier to understand and debug.
- **Configuration via JSON**: Defines workflows through a JSON configuration file for easy customization and scalability.
- **Error Handling**: Custom exception handling ensures robust and reliable execution.

## Technologies Used

- **Language**: Python 3.8+
- **Libraries**:
  - `aiohttp` - Asynchronous HTTP client/server framework
  - `asyncio` - Asynchronous I/O, event loop, coroutines and tasks
  - `nest_asyncio` - Nested event loop support
  - `python-dotenv` - Environment variable management
  - `colorama` - Cross-platform colored terminal text
  - `graphviz` - Graph visualization software
  - `IPython` - Enhanced interactive Python shell
  - `beautifulsoup4` - Web scraping library
  - `tiktoken` - Fast BPE tokenizer for OpenAI models
  - `numpy` - Numerical computing library
  - `fpdf` - PDF generation library

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/simonpierreboucher02/LLMFLOW-main.git
cd LLMFLOW-main
```

### 2. Create a Virtual Environment and Activate It

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project and add your API keys:

```env
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

**Note**: Ensure that the `.env` file is included in your `.gitignore` to prevent sensitive information from being committed to version control.

## Configuration

### Environment Variables

The `.env` file holds your API keys necessary for interacting with different LLM providers. Ensure that each key is correctly set:

```env
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

### Flow Configuration

Define your workflow steps and blocks in a `config.json` file. This JSON file specifies the sequence of prompts, models to use, input dependencies, and output saving options.

#### Example `config.json`

```json
{
    "steps": [
        {
            "blocks": [
                {
                    "prompt": "Generate a multiple-choice question about portfolio management with three answer choices.",
                    "model": "gpt-4o-mini",
                    "max_tokens": 150,
                    "temperature": 0.7,
                    "save_output": {
                        "format": "txt",
                        "filename": "question_1.txt"
                    }
                }
            ]
        },
        {
            "blocks": [
                {
                    "prompt": "Based on the previously generated question: [insert question_1.txt output here], generate a new multiple-choice question about portfolio management.",
                    "model": "gpt-4o-mini",
                    "max_tokens": 150,
                    "temperature": 0.7,
                    "inputs": [[0, 0]],
                    "save_output": {
                        "format": "txt",
                        "filename": "question_2.txt"
                    }
                }
            ]
        },
        {
            "blocks": [
                {
                    "prompt": "Based on the previously generated question: [insert question_2.txt output here], generate a new multiple-choice question about portfolio management.",
                    "model": "gpt-4o-mini",
                    "max_tokens": 150,
                    "temperature": 0.7,
                    "inputs": [[1, 0]],
                    "save_output": {
                        "format": "txt",
                        "filename": "question_3.txt"
                    }
                }
            ]
        },
        // Add more steps as needed
        {
            "blocks": [
                {
                    "prompt": "Compile the previously generated questions: [insert all question outputs here]. Format them into a multiple-choice exam report on portfolio management and save as a PDF.",
                    "model": "gpt-4o-mini",
                    "max_tokens": 2000,
                    "temperature": 0.7,
                    "inputs": [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],
                    "save_output": {
                        "format": "pdf",
                        "filename": "portfolio_management_exam.pdf"
                    }
                }
            ]
        }
    ]
}
```

**Explanation of Fields**:

- **steps**: An array of workflow steps.
- **blocks**: An array of tasks within each step.
- **prompt**: The prompt sent to the LLM.
- **model**: The specific LLM model to use (e.g., `gpt-4o-mini`).
- **max_tokens**: Maximum number of tokens to generate.
- **temperature**: Sampling temperature for text generation.
- **inputs**: References to outputs from previous blocks in the format `[step_index, block_index]`.
- **save_output**: Configuration for saving the output.
  - **format**: The format to save (`txt`, `pdf`).
  - **filename**: The name of the output file.

## Usage

### Running the Flow

Execute the main script to start the workflow defined in your `config.json`:

```bash
python run.py
```

### Description of Workflow Execution

1. **Initialization**: Loads environment variables and configures logging.
2. **Flow Creation**: Parses `config.json` to create a series of steps and blocks.
3. **Processing Steps**: Iterates through each step, executing each block asynchronously.
   - **Loading External Data**: Fetches any required external data (e.g., web pages, APIs).
   - **Semantic Search**: Enhances prompts based on semantic relevance.
   - **Text Generation**: Sends prompts to the specified LLM and retrieves responses.
   - **Saving Outputs**: Saves generated outputs in the specified formats.
4. **Flow Visualization**: Generates a visual representation of the workflow using Graphviz.
5. **Results Display**: Prints the outputs of each block to the console.

## Project Structure

```
LLMFLOW-main/
├── run.py
├── config.json
├── requirements.txt
├── .env
├── README.md
├── .gitignore
└── src/
    ├── __init__.py
    ├── api/
    │   ├── __init__.py
    │   ├── model_api.py
    │   └── api_client.py
    ├── flow/
    │   ├── __init__.py
    │   ├── prompt_block.py
    │   ├── step.py
    │   ├── semantic_search.py
    │   └── flow_manager.py
    └── utils/
        ├── __init__.py
        ├── token_utils.py
        ├── config.py
        └── exceptions.py
```

### Description of Directories and Files

- **run.py**: The main entry point of the application.
- **config.json**: JSON file defining the workflow steps and blocks.
- **requirements.txt**: Lists all Python dependencies.
- **.env**: Environment variables file containing API keys.
- **README.md**: Project documentation.
- **.gitignore**: Specifies files and directories to be ignored by Git.

#### Directory `src/`

- **api/**: Contains classes for interacting with different LLM APIs.
  - **model_api.py**: Defines abstract and concrete classes for each LLM provider.
  - **api_client.py**: Manages API calls and handles token limits and splitting prompts.
- **flow/**: Manages the workflow execution.
  - **prompt_block.py**: Defines the `PromptBlock` class for individual tasks.
  - **step.py**: Defines the `Step` class for grouping blocks.
  - **semantic_search.py**: Implements semantic search functionality.
  - **flow_manager.py**: Orchestrates the entire workflow, managing steps and blocks.
- **utils/**: Utility functions and classes.
  - **token_utils.py**: Calculates the number of tokens in a string.
  - **config.py**: Loads and parses the configuration file.
  - **exceptions.py**: Defines custom exceptions for the framework.

## Example Use Case

### Multiple-Choice Question Generator

This example demonstrates how to use the LLM Flow Framework to generate a series of multiple-choice questions and compile them into a PDF report.

1. **Step 1 to 10**: Generate ten sequential multiple-choice questions about portfolio management. Each question is based on the previous one.
2. **Step 11**: Compile all generated questions into a formatted PDF report suitable for use as an exam or quiz.

**Output**:

- **question_1.txt** to **question_10.txt**: Text files containing each generated question.
- **portfolio_management_exam.pdf**: A compiled PDF report of all questions.

## Extending the Framework

The LLM Flow Framework is designed to be highly extensible. Here's how you can customize and extend its capabilities:

### Adding New External Data Sources

1. **Define a New External Data Class**: In `src/api/model_api.py`, create a new class inheriting from `ExternalData` to handle different data sources.

   ```python
   class NewDataType(ExternalData):
       async def load_data(self, session: aiohttp.ClientSession) -> str:
           # Implement data loading logic
           pass
   ```

2. **Update Configuration**: Modify `config.json` to include the new data type.

   ```json
   {
       "external_data": {
           "type": "new_data_type",
           "source": "your_data_source"
       }
   }
   ```

### Supporting Additional Output Formats

1. **Extend `OutputSaver`**: In `src/flow/prompt_block.py`, add methods to handle new formats.

   ```python
   class OutputSaver:
       @staticmethod
       def save_new_format(content: str, filename: str):
           # Implement saving logic
           pass
   ```

2. **Update `PromptBlock`**: Modify the `save_block_output` method to handle the new format.

   ```python
   if output_format == 'new_format':
       OutputSaver.save_new_format(self.output, filename)
   ```

### Integrating Additional LLM Providers

1. **Create a New API Class**: In `src/api/model_api.py`, define a new class for the additional LLM provider.

   ```python
   class NewLLMAPI(ModelAPI):
       def __init__(self, api_key: str):
           self.api_key = api_key

       async def generate_text(self, session: aiohttp.ClientSession, model: str, prompt: str, 
                               temperature: float, max_tokens: int) -> Dict[str, Any]:
           # Implement API call
           pass

       def extract_text_from_response(self, response: Dict[str, Any]) -> str:
           # Implement response extraction
           pass

       async def get_embeddings(self, session: aiohttp.ClientSession, texts: List[str]) -> List[List[float]]:
           # Implement embeddings retrieval if supported
           pass
   ```

2. **Update `APIClient`**: In `src/api/api_client.py`, include the new LLM provider.

   ```python
   self.apis = {
       "openai": OpenAIAPI(api_keys.get("openai")),
       "anthropic": AnthropicAPI(api_keys.get("anthropic")),
       "mistral": MistralAPI(api_keys.get("mistral")),
       "newllm": NewLLMAPI(api_keys.get("newllm"))
   }
   ```

3. **Update Configuration**: Specify the new model in `config.json`.

   ```json
   {
       "model": "newllm-model-name",
       // other fields
   }
   ```

## Contribution

Contributions are welcome! Follow these steps to contribute to the LLM Flow Framework:

1. **Fork the Repository**

   Click the "Fork" button at the top-right corner of the repository page to create a copy of the repository under your GitHub account.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/LLMFLOW-main.git
   cd LLMFLOW-main
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**

   Implement your feature or bug fix.

5. **Commit Your Changes**

   ```bash
   git commit -m "Add feature: your feature description"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**

   Go to the original repository on GitHub and click "New Pull Request". Provide a clear description of your changes and submit the pull request.

**Note**: Please ensure your code adheres to the project's coding standards and that all new features are thoroughly tested.

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for providing powerful language models.
- [Anthropic](https://www.anthropic.com/) for their contributions to AI safety and research.
- [Mistral](https://mistral.ai/) for their innovative language model solutions.
- Contributors of the Python libraries used in this project.

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/simonpierreboucher02">Simon Pierre Boucher</a></p>
  <p>⭐ Star this repository if you found it helpful!</p>
</div>

