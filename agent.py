# Importing Required Modules
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

# Loading Environment Variables
# tool enables real-time web search capabilities using DuckDuckGo
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


# Initializing the Agent
agent=Agent(
    model=Groq(id="llama-3.2-3b-preview"),
    description="You are an assistant please reply based on the question",
    tools=[DuckDuckGoTools()],
    markdown=True
)


# The agent processes the query using:
# 1. Groq’s LLaMA 3 model (70B).
# 2. DuckDuckGo search (if needed) for up-to-date information.
agent.print_response("Who was champions trophy 2025 winner")