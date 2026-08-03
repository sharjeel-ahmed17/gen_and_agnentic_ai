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
    model = "embed-english-light-v3.0",
    provider="cohere"
)
client = QdrantClient(":memory:")

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
result = vector_store.similarity_search("what is used for data analysis?",k=2)

for r in result:
    print(r.page_content)
    print(r.metadata)

retriver = vector_store.as_retriever()

docs = retriver.invoke("Explain deep learning")

for d in docs:
    print(d.page_content)