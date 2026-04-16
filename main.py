from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


openai_api_key = os.getenv("OPENAI_API_KEY")

def main():
    
    information = """
    Elon Musk is a well-known entrepreneur, 
    inventor, and business magnate. 
    He was born on June 28, 1971, in South Africa. 
    Musk is the CEO of Tesla, where he leads the development of electric cars and clean energy solutions,
    and also the founder of SpaceX, which focuses on space exploration and reusable rockets. He has also been involved in companies like Neuralink and The Boring Company. 
    Musk is known for his ambitious vision to colonize Mars, reduce global warming, and advance technology for the future."""

    summary_template = """
    Given the following information, provide a concise summary of the text.
    
    Information: {information}
    
    Summary: """

    prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature= 0, model = "gpt-4o", api_key=openai_api_key)

    chain = prompt_template | llm

    response = chain.invoke({"information": information})

    print(response.content)


if __name__ == "__main__":
    main()