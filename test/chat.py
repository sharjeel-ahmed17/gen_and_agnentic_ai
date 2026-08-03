from dotenv import load_dotenv
load_dotenv(override=True)
from langchain.chat_models import init_chat_model
from rich import print

model = init_chat_model(
    base_url="",
    api_key="",
    model = "",
    model_provider="openai",
    temperature=0.9
    )
response = model.invoke("write a poem on AI")
print(response.content)