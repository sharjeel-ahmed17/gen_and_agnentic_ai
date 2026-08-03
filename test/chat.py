from dotenv import load_dotenv
from rich import print
from langchain.chat_models import init_chat_model

load_dotenv(override=True)

model = init_chat_model(
    base_url="",
    api_key="",
    model = "",
    model_provider="openai",
    temperature=0.9
    )
response = model.invoke("write a poem on AI")
print(response.content)