from langchain_ollama import ChatOllama
from utils.config import OLLAMA_MODEL

local_llm = ChatOllama(model=OLLAMA_MODEL, temperature=0)
