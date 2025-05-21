# 🌍 LLM Translator (LangChain + OpenAI + LangSmith)

A simple and interactive CLI tool to translate English text into any target language using OpenAI's GPT models via LangChain, with full tracing enabled using LangSmith.

---

## ✨ Features

- 🌐 Translate English text into any language (default: Italian)
- ⚡ Powered by OpenAI’s GPT models (e.g., `gpt-4o-mini`, `gpt-3.5-turbo`)
- 🧠 Built with [LangChain](https://www.langchain.com/)
- 📊 Integrated with [LangSmith](https://smith.langchain.com/) for trace inspection and debugging
- 💻 Clean and user-friendly CLI
- 🔧 Easily extendable for batch processing or file-based translations

---

## 📦 Requirements

- Python 3.8+
- OpenAI API Key
- LangSmith API Key (optional but recommended for debugging)

---

## 🚀 Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/rehmat11872/LLM-Translator.git
    cd LLM-Translator
    ```

2. **Create a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** (optional for LangSmith)

    ```env
    OPENAI_API_KEY=your-openai-api-key
    LANGSMITH_API_KEY=your-langsmith-api-key
    LANGSMITH_TRACING=true
    LANGSMITH_ENDPOINT=https://api.smith.langchain.com
    ```