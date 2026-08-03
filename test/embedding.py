from dotenv import load_dotenv
from langchain.embeddings import init_embeddings
load_dotenv(override=True)
from rich import print

embeddings = init_embeddings(
    model = "",
    provider=""
)
texts = [
    "Hello this is Akarsh Vyas",
    "Hello your name is YouTube",
    "And you all are very beautiful"
]
vector = embeddings.embed_documents(texts)
if __name__ == "__main__":
    print(vector)