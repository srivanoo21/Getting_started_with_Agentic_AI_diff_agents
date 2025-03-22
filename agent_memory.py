# Importing Required Libraries
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.embedder.openai import OpenAIEmbedder
from sentence_transformers import SentenceTransformer
from agno.embedder.base import Embedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase # Loads knowledge from a PDF file.
from agno.vectordb.lancedb import LanceDb, SearchType # to store and retrieve embedded knowledge efficiently
from dotenv import load_dotenv
import os


# Custom Hugging Face Embedder (Fix: Implemented `get_embedding_and_usage`)
class HFEmbedder(Embedder):
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text: str):
        """Returns the embedding vector for the given text."""
        return self.model.encode(text).tolist()

    def get_embedding_and_usage(self, text: str):
        """Returns the embedding and a placeholder for usage statistics."""
        return self.get_embedding(text), None  # Usage stats are not provided
    

# Loading Environment Variables
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


# Defining the AI Agent
# This defines an AI-powered agent that specializes in Thai cuisine by leveraging a knowledge base, 
# a vector database (LanceDb), and web search capabilities (DuckDuckGoTools). 
# knowledge - Loads a Thai Recipes PDF from a URL and stores its data in the agent’s knowledge base. The agent
#             can retrieve relevant content directly from the PDF.
# vector_db - Stores the PDF content in a vector database (LanceDb), enabling semantic search
agent = Agent(
    model=Groq(id="llama-3.2-3b-preview"),
    description="You are a Thai cuisine expert!",
    instructions=[
        "Search your knowledge base for Thai recipes.",
        "If the question is better suited for the web, search the web to fill in gaps.",
        "Prefer the information in your knowledge base over the web results."
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb", # Stores the database in a temporary location
            table_name="recipes", # Creates a table named "recipes" for structured storage
            search_type=SearchType.hybrid, # Uses both exact match & semantic search
            embedder=HFEmbedder(model_name="sentence-transformers/all-MiniLM-L6-v2"), # Uses OpenAI's embedding model to convert text into vectors
        ),
    ),
    tools=[DuckDuckGoTools()], # If the knowledge base lacks data, the agent can search the web in real-time using DuckDuckGo

    show_tool_calls=True, # Logs tool usage, showing when the agent calls the knowledge base or web search
    markdown=True # Formats responses in markdown, improving readability
)


# Loading the Knowledge Base (First Run) - use below section only 1st time and then we can comment it
# This can be commented out after the knowledge base is loaded

# if agent.knowledge is not None:
#     print("INFO: Loading Knowledge Base...")
#     agent.knowledge.load()
#     print("INFO: Knowledge Base Loaded Successfully!")


# Sample Queries
print("\n✅ Querying Agent:")
try:
    agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
except Exception as e:
    print("⚠️ Error occurred:", e)

try:
    agent.print_response("What is the history of Thai curry?", stream=True)
except Exception as e:
    print("� Error occurred:", e)
