from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS

def create_vector_store(documents, folder="models/faiss_index"):
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    texts = [doc.page_content for doc in documents]
    embeddings = model.encode(texts)

    db = FAISS.from_embeddings(embeddings, texts)
    db.save_local(folder)

    return db
