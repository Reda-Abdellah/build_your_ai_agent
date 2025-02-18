import os

# OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "your-default-key")
POSTGRES_URI = os.getenv("POSTGRES_URI", "postgresql://user:password@localhost/dbname")
CHROMA_COLLECTION_NAME = "your_collection"
# Environment variables
os.environ['NO_PROXY'] = "http://127.0.0.1,localhost"

# OLLAMA_MODEL= "deepseek-r1:latest" #Not compatible with tools
OLLAMA_MODEL= "qwen2.5:32b"

ENABLE_POSTGRES = True
# PostgreSQL connection details (default values)
POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")  # Replace with your actual password
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "testdb")
POSTGRES_TABLE = os.getenv("POSTGRES_TABLE", "mock_data_table")