from dotenv import load_dotenv
from rich import print
from langchain.embeddings import init_embeddings
load_dotenv(override=True)
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