from langchain_community.document_loaders import WebBaseLoader

url = "https://www.apple.com/in/macbook-pro/"
data = WebBaseLoader(url)
docs = data.load()
if __name__ == "__main__":
    print(docs[0].page_content)