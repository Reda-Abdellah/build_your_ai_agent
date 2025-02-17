import os

# OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "your-default-key")
POSTGRES_URI = os.getenv("POSTGRES_URI", "postgresql://user:password@localhost/dbname")
CHROMA_COLLECTION_NAME = "your_collection"
# Environment variables
os.environ['NO_PROXY'] = "http://127.0.0.1,localhost"

# OLLAMA_MODEL= "deepseek-r1:latest" #Not compatible with tools
OLLAMA_MODEL= "qwen2.5:32b" 