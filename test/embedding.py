from dotenv import load_dotenv
from rich import print
from langchain.embeddings import init_embeddings
from langchain_community.embeddings import FastEmbedEmbeddings
load_dotenv(override=True)

fastembed = FastEmbedEmbeddings(
    model_name='BAAI/bge-small-en-v1.5'
)
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