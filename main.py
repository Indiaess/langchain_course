from dotenv import load_dotenv
import os

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from tavily import TavilyClient


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

tavily = TavilyClient(api_key=tavily_api_key)  

@tool
def search(query: str) -> str:
    """Search the web for information"""
    print(f"Searching for {query}")

    response = tavily.search(query=query,search_depth="advanced")
    return response["results"][0]["content"]


llm = ChatOpenAI(model = "gpt-4o", temperature = 0)

tools = [search]

agent = create_agent(model = llm, tools = tools)


def main():
    response = agent.invoke({"messages": [{"role": "user", "content": "Who won the IPL match on 15th April 2026 between LSG and RCB? And from how many runs? Who batted first and what was the score of LSG in powerplay"}]})
    print(response["messages"][-1].content)

if __name__ == "__main__":
    main()


 