# 🧠 AI_Research_Assistant_Agent

> An intelligent multi-agent research assistant powered by Large Language Models, Retrieval-Augmented Generation (RAG), and LangGraph for document understanding, reasoning, and tool-assisted analysis.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge)
![LangGraph](https://img.shields.io/badge/LangGraph-4B8BBE?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-6E40C9?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge\&logo=openai\&logoColor=white)
![License](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)

---

# 📖 Description

ResearchMind AI is a production-inspired AI research assistant that combines **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, **Vector Databases**, **AI Agents**, and **Tool Calling** to answer complex user queries using both private documents and external tools.

Instead of relying solely on an LLM's internal knowledge, the system retrieves relevant information from uploaded documents, performs multi-step reasoning, invokes tools when necessary, and generates accurate, context-aware responses.

The project is designed to demonstrate modern AI Engineering concepts and production-ready architecture while remaining modular, scalable, and easy to extend.

---

# ❗ Problem

Traditional LLM-based chatbots suffer from several limitations:

* Limited knowledge beyond their training data
* Hallucinated or fabricated responses
* Inability to access private documents
* Lack of long-term conversational memory
* No capability to perform external actions or use tools
* Difficulty solving multi-step reasoning tasks

These limitations make standard chatbots unsuitable for research-intensive or enterprise use cases.

---

# 💡 Solution

ResearchMind AI addresses these challenges by integrating several modern AI techniques into a unified system.

The application:

* Understands user intent using an LLM
* Retrieves relevant information from uploaded documents using RAG
* Stores semantic document embeddings in a vector database
* Maintains conversational memory for contextual interactions
* Uses AI Agents to plan and execute multi-step tasks
* Invokes external tools (calculator, search, etc.) when required
* Produces grounded, explainable, and context-aware responses

---

# ✨ Features

* 📄 Intelligent PDF document ingestion
* 🔍 Semantic document search using embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 Multi-Agent workflow powered by LangGraph
* 🛠️ Tool Calling for external capabilities
* 💬 Conversation memory
* ⚡ FastAPI backend
* 🎨 Streamlit frontend
* 📊 Modular and scalable architecture
* 🔒 Environment-based configuration
* 📦 Ready for containerization and deployment

---

# 🚀 Tech Stack

| Category                  | Technologies                       |
| ------------------------- | ---------------------------------- |
| **Language**              | Python 3.12                        |
| **LLM Framework**         | LangChain                          |
| **Agent Framework**       | LangGraph                          |
| **Language Models**       | OpenAI GPT / Ollama (Local Models) |
| **RAG Pipeline**          | LangChain Retrieval                |
| **Embeddings**            | OpenAI Embeddings                  |
| **Vector Database**       | ChromaDB                           |
| **Backend API**           | FastAPI                            |
| **Frontend**              | Streamlit                          |
| **Configuration**         | python-dotenv                      |
| **Tokenization**          | tiktoken                           |
| **HTTP Client**           | httpx                              |
| **PDF Processing**        | PyPDF                              |
| **Dependency Management** | uv                                 |
| **Version Control**       | Git & GitHub                       |

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ResearchMind-AI.git
```

```bash
cd ResearchMind-AI
```

---

## 2. Create a virtual environment

```bash
uv venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
uv sync
```

---

## 4. Configure environment variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_api_key_here
```

---

## 5. Run the backend

```bash
uv run uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🛣️ Roadmap

* [x] Project setup
* [x] FastAPI backend
* [x] OpenAI integration
* [x] Prompt templates
* [x] PDF ingestion
* [x] Text chunking
* [x] Embeddings
* [x] ChromaDB integration
* [x] Retrieval-Augmented Generation
* [ ] AI Agent with LangGraph
* [ ] Tool Calling
* [ ] Conversation Memory
* [ ] Streamlit UI
* [ ] Docker support
* [ ] Deployment

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

If you find a bug or have an improvement in mind, feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

See the `LICENSE` file for more information.
