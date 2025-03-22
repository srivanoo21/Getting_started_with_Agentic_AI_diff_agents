# Importing Necessary Modules
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools # Enables real-time web search
from agno.tools.yfinance import YFinanceTools # Fetches financial data
from dotenv import load_dotenv
import os


# Loading Environment Variables
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


# Creating the Web Search Agent - Fetches the latest news on these companies
web_agent=Agent(
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="llama-3.2-3b-preview"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True,
)

# Creating the Finance Agent - Gets stock prices, fundamentals, and recommendations
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

# Creating a Team of Agents
agent_team=Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="llama-3.2-3b-preview"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,

)

agent_team.print_response("Analyze companies like Tesla,NVDA,Apple and suggest which to buy for long term")