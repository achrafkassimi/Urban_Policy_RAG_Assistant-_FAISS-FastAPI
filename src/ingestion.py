import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader

def load_documents(folder="data/raw"):
    docs = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())

        elif file.endswith(".docx"):
            docs.extend(Docx2txtLoader(path).load())

    return docs


def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
    return splitter.split_documents(docs)
