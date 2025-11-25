import streamlit as st
import requests

st.title("🧠 RAG Intelligent Policy Assistant")

q = st.text_input("Posez votre question:")

if st.button("Envoyer"):
    r = requests.post("http://localhost:8000/ask", json={"question": q})
    st.write("### ✨ Réponse:")
    st.write(r.json()["answer"])
