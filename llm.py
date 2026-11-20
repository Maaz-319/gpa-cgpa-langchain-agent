from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

llm = init_chat_model(
    os.getenv("MODEL"),
    model_provider="openai",
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)