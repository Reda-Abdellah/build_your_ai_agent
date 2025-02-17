# AI Agent with LangGraph and Streamlit

This project implements an AI agent using LangGraph that connects to a local LLM served by Ollama. The agent can perform various tasks such as retrieving information from a browser, querying PostgreSQL databases, retrieving context from ChromaDB (RAG), calling Python functions, and interacting with web APIs.

## Features

- **Local LLM**: Powered by Ollama for privacy and cost efficiency.
- **Tool Integration**: Includes web search, database queries, RAG via ChromaDB, Python function calls, and web APIs.
- **Session Persistence**: Maintains conversation history across sessions.
- **Streamlit Frontend**: Simple UI for user interaction.

## Requirements

Install dependencies using:
pip install -r requirements.txt

## Run the Application

Start the Streamlit app:
streamlit run main.py


## Project Structure

- `main.py`: Entry point for the Streamlit app.
- `agent/`: Contains tools, LLM setup, and LangGraph workflow definition.
- `utils/`: Helper functions and configuration settings.
- `data/`: Stores local data files like embeddings or SQLite databases.

## Future Enhancements

- Add more tools for advanced functionality.
- Support asynchronous responses for long-running tasks.

