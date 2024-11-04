import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq
from langchain.chains import ConversationChain
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory

load_dotenv()

api_key = os.getenv("LLM_API_KEY")
client = Groq(api_key=api_key)

embedding_model = OpenAIEmbeddings(openai_api_key=api_key)
memory = ConversationBufferMemory()

st.title("Chatbot Interativo")

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

user_input = st.text_input("Você: ")

if st.button("Enviar"):
    if user_input:
        if st.session_state.vector_store is None:
            st.session_state.vector_store = FAISS.from_texts([user_input], embedding_model)
        else:
            st.session_state.vector_store.add_texts([user_input])

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-8b-8192",  
            stream=False,
        )
        
        response = chat_completion.choices[0].message.content
        st.text("Chatbot: " + response)
