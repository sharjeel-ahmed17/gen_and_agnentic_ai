import os
from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_core.documents import Document
from langchain.embeddings import init_embeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

embeddings = init_embeddings(
    model="embed-english-light-v3.0",
    provider="cohere"
)

# docker run -d -p 6333:6333 -p 6334:6334 -v qdrant_storage:/qdrant/storage qdrant/qdrant

# client = QdrantClient(":memory:")
# client = QdrantClient(path="./qdrant_data")
# client = QdrantClient(
#     url=os.getenv("QDRANT_URL"),
#     api_key=os.getenv("QDRANT_API_KEY")
# )
client = QdrantClient(
    url=os.getenv("QDRANT_URL", "http://localhost:6333")
)
try:
    # Check karein ke collection pehle se exist karti hai ya nahi
    if not client.collection_exists(collection_name="demo_collection"):
        client.create_collection(
            collection_name="demo_collection",
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

    vector_store = QdrantVectorStore(
        client=client,
        embedding=embeddings,
        collection_name="demo_collection"
    )

    vector_store.add_documents(documents=docs)
    result = vector_store.similarity_search("what is used for data analysis?", k=2)

    for r in result:
        print(r.page_content)
        print(r.metadata)

    retriever = vector_store.as_retriever()
    retrieved_docs = retriever.invoke("Explain deep learning")

    for d in retrieved_docs:
        print(d.page_content)

finally:
    # Explicitly client close hoga chahe error aaye ya na aaye
    client.close()