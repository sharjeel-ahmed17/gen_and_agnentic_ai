import os
from typing import Literal
from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_core.documents import Document
from langchain.embeddings import init_embeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_community.embeddings import FastEmbedEmbeddings

fastembed = FastEmbedEmbeddings(
    model_name='BAAI/bge-small-en-v1.5'
)

def get_vector_store(
    collection_name: str,
    embedding_model,
    mode: Literal["in_memory", "local_disk", "local_docker", "production"] = "in_memory",
    vector_size: int = 384,
) -> tuple[QdrantVectorStore, QdrantClient]:
    if mode == "in_memory":
        client = QdrantClient(":memory:")

    elif mode == "local_disk":
        client = QdrantClient(path="./qdrant_data")

    elif mode == "local_docker":
        qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
        client = QdrantClient(url=qdrant_url)

    elif mode == "production":
        qdrant_url = os.getenv("QDRANT_URL")
        api_key = os.getenv("QDRANT_API_KEY")

        if not qdrant_url or not api_key:
            raise ValueError("Production mode ke liye QDRANT_URL aur QDRANT_API_KEY zaruri hain.")

        client = QdrantClient(url=qdrant_url, api_key=api_key)

    else:
        raise ValueError("Invalid mode!")

    if not client.collection_exists(collection_name=collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size, distance=Distance.COSINE
            ),
        )

    vector_store = QdrantVectorStore(
        client=client,
        embedding=embedding_model,
        collection_name=collection_name,
    )

    return vector_store, client


docs = [
    Document(
        page_content="Python is widely used in Artificial Intelligence.",
        metadata={"source": "AI_book"},
    ),
    Document(
        page_content="Pandas is used for data analysis in Python.",
        metadata={"source": "DataScience_book"},
    ),
    Document(
        page_content="Neural networks are used in deep learning.",
        metadata={"source": "DL_book"},
    ),
]

embeddings = init_embeddings(
    model="embed-english-light-v3.0", provider="cohere"
)

vector_store, client = get_vector_store(
    collection_name="demo_collection",
    embedding_model=embeddings,
    mode="local_docker",
)

try:
    vector_store.add_documents(documents=docs)

    print("--- Similarity Search Result ---")
    result = vector_store.similarity_search(
        "what is used for data analysis?", k=2
    )
    for r in result:
        print(r.page_content)
        print(r.metadata)

    print("\n--- Retriever Result ---")
    retriever = vector_store.as_retriever()
    retrieved_docs = retriever.invoke("Explain deep learning")
    for d in retrieved_docs:
        print(d.page_content)

finally:
    client.close()