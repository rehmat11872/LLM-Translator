from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model       
from langchain_core.prompts import ChatPromptTemplate    
import logging
logging.basicConfig(level=logging.INFO)

# 1) choose a chat model (change to gpt-3.5-turbo etc. if you like)
model = init_chat_model("gpt-4o-mini", model_provider="openai")

# 2) build a reusable prompt template
system_tpl = "Translate the following from English into {language}"
prompt_tpl = ChatPromptTemplate.from_messages(
    [("system", system_tpl), ("user", "{text}")]
)

def translate(text: str, language: str = "Italian") -> str:
    """Return the LLM translation of text → language."""
    prompt = prompt_tpl.invoke({"language": language, "text": text})
    response = model.invoke(prompt)
    logging.info(f"Response: {response}")
    return response.content.strip()

if __name__ == "__main__":
    src = input("English text ➜ ")
    tgt_lang = input("Target language (default Italian) ➜ ") or "Italian"
    print("🔁  Translating…")
    print(translate(src, tgt_lang))
