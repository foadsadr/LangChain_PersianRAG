
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM - it will automatically use the OPENAI_API_KEY from environment variables
llm = ChatOpenAI()
llm.invoke("Hello, world!")