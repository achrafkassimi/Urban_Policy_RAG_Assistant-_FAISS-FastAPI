from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain.llms import OpenAI  # or HuggingFace endpoint model

class RAGEngine:
    def __init__(self, index_path="models/faiss_index"):
        self.emb_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.db = FAISS.load_local(index_path, self.emb_model)

    def query(self, question):
        docs = self.db.similarity_search(question, k=3)
        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
        You are an expert in urban policy.
        Use ONLY the context below to answer.

        CONTEXT:
        {context}

        QUESTION:
        {question}

        Answer:
        """

        llm = OpenAI(temperature=0)   # Replace with local or HF model
        return llm(prompt)
