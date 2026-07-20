import streamlit as st
import requests


BACKEND_URL = "http://127.0.0.1:8000/chat"


st.set_page_config(
    page_title="ResearchMind",
    page_icon="🧠",
)

st.title("🧠 ResearchMind")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages: # type: ignore
    with st.chat_message(message["role"]): # type: ignore
        st.markdown(message["content"]) # type: ignore


prompt = st.chat_input("Ask anything...")

if prompt:

    st.session_state.messages.append( # type: ignore
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = requests.post(
                BACKEND_URL,
                json={
                    "message": prompt
                },
            )

            answer = response.json()["answer"]

            st.markdown(answer)

    st.session_state.messages.append( # type: ignore
        {
            "role": "assistant",
            "content": answer,
        }
    )