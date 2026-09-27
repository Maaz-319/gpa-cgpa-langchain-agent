from langchain.chat_models import init_chat_model
from os import getenv
from dotenv import load_dotenv
load_dotenv()
llm = init_chat_model("groq:openai/gpt-oss-20b", api_key=getenv("GROQ_API_KEY"))