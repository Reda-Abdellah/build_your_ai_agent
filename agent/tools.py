# from langchain.vectorstores import Chroma
from langchain_experimental.sql import SQLDatabaseChain
from langchain.utilities.sql_database import SQLDatabase
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun

from utils.config import ENABLE_POSTGRES, POSTGRES_DATABASE, POSTGRES_HOST, POSTGRES_PASSWORD, POSTGRES_PORT, POSTGRES_USERNAME
from langchain_core.tools import tool


def get_web_search_tool():
    tool = DuckDuckGoSearchRun(max_results=4)  # Define the DuckDuckGo search tool
    return tool


def create_postgres_tool(local_llm):
    @tool
    def postgres_tool(query: str) -> str:
        """
        Executes the given SQL query on the PostgreSQL database.
        Args:
            query (str): The SQL query to execute.
        Returns:
            str: The result of the query execution.
        """
        # Replace these placeholders with your actual PostgreSQL credentials
        POSTGRES_URI = (
            f"postgresql+psycopg2://{POSTGRES_USERNAME}:"
            f"{POSTGRES_PASSWORD}@{POSTGRES_HOST}:"
            f"{POSTGRES_PORT}/{POSTGRES_DATABASE}"
        )
        # Create an SQLDatabase instance and SQLDatabaseChain
        db = SQLDatabase.from_uri(POSTGRES_URI)
        chain_tool = SQLDatabaseChain.from_llm(local_llm, db)
        
        # Execute the query and return results
        return chain_tool.run(query)
    
    return postgres_tool

# def chroma_rag_tool(state):
#     query = state.get("query", "")
#     chroma_db = Chroma(embedding_function=your_embedding_model, collection_name="your_collection")
#     documents = chroma_db.as_retriever().get_relevant_documents(query)
#     return {"context_docs": documents}

def get_tools(llm):
    # Define the list of tools with the web search tool as default
    tools = [get_web_search_tool()]

    # Conditionally add the Postgres tool if ENABLE_POSTGRES is True
    if ENABLE_POSTGRES:
        tools.append(create_postgres_tool(llm))
    return tools