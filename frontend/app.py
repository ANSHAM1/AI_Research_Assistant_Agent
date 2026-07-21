import streamlit as st
import requests

from pathlib import Path

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

css = Path(__file__).parent / "styles.css"

with open(css) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("📚 Knowledge Base")

    rag_files = st.file_uploader(
        "Upload documents for RAG",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Index Documents", use_container_width=True):

        if rag_files:

            files = [
                (
                    "files",
                    (f.name, f.getvalue(), f.type)
                )
                for f in rag_files
            ]

            with st.spinner("Indexing..."):
                response = requests.post(
                    f"{API_URL}/rag/upload",
                    files=files
                )

            if response.status_code == 200:
                st.success("Knowledge Base Updated")
            else:
                st.error("Failed")

        else:
            st.warning("Upload at least one file.")

    st.divider()

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# -----------------------------
# Header
# -----------------------------

st.title("🤖 AI Research Assistant")
st.caption("Chat • RAG • File Understanding")

# -----------------------------
# Chat History
# -----------------------------

for message in st.session_state.messages: # type: ignore

    with st.chat_message(message["role"]): # type: ignore

        st.markdown(message["content"]) # type: ignore

        if "attachments" in message:

            for file in message["attachments"]: # type: ignore
                st.caption(f"📎 {file}")


# -----------------------------
# Chat Input
# -----------------------------

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

    payload = {
        "question": prompt
    }

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = requests.post(
                f"{API_URL}/chat",
                data=payload
            )

            if response.status_code == 200:

                answer = response.json()["answer"]

            else:

                answer = "Backend Error"

        st.markdown(answer)

    st.session_state.messages.append( # type: ignore
        {
            "role": "assistant",
            "content": answer
        }
    )