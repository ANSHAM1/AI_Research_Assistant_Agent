# 🧠 ResearchMind AI

> An intelligent AI research assistant powered by LLMs, RAG, and LangGraph for document understanding, reasoning, and context-aware answers.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge)
![LangGraph](https://img.shields.io/badge/LangGraph-4B8BBE?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-6E40C9?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

# 📖 Overview

ResearchMind AI is a production-inspired AI research assistant that combines:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- LangGraph workflows
- Tool-assisted reasoning (AI Agent)
- Conversation/session memory

The system allows users to upload documents, retrieve relevant information, and generate grounded answers instead of relying only on an LLM's internal knowledge.

---

# ❗ Problem

Traditional LLM chatbots have limitations:

- No access to private documents
- Hallucinated information
- No semantic document search
- Limited reasoning capabilities
- No persistent conversation context

---

# 💡 Solution

ResearchMind AI addresses these challenges by integrating several modern AI techniques into a unified system.

The application:

* Understands user intent using an LLM
* Retrieves relevant information from uploaded documents using RAG
* Stores semantic document embeddings in a vector database
* Maintains conversational memory for contextual interactions
* Uses AI Agents to plan and execute multi-step tasks(calculation, web search)
* Produces grounded, explainable, and context-aware responses

---

# 🏗️ LangGraph Workflow

The assistant uses a conditional LangGraph workflow:

1. User sends a question.
2. Router LLM determines whether Retrieval-Augmented Generation (RAG) is required.
3. If RAG is required:
   - Retrieve relevant documents from ChromaDB.
   - Store the retrieved context in the graph state.
4. The chatbot LLM generates a response.
5. If the LLM requests a tool:
   - Execute the appropriate tool.
   - Return the tool result to the chatbot.
   - Generate the final response.
6. Return the answer to the user.

Flow:

    START
      |
      v
    router_node
      |
      |---- no rag ----> chatbot_node ----+
      |                                   |
      |                           Tool Required?
      |                            /         \
      |                          Yes         No
      |                           |           |
      |                           v           v
      |                      tool_node       END
      |                           |
      |                           v
      |                     chatbot_node
      |                           |
      |                           v
      |                          END
      |
      |---- rag -------> rag_node
                            |
                            v
                       chatbot_node
                            |
                     Tool Required?
                       /         \
                     Yes         No
                      |           |
                      v           v
                 tool_node       END
                      |
                      v
                chatbot_node
                      |
                      v
                     END

---

# 🧩 Final Graph Architecture

                          START
                            |
                            v
                      router_node
                     /            \
                USE_RAG         NO_RAG
                   |               |
                   v               |
              rag_node             |
                   |               |
                   +-------+-------+
                           |
                           v
                     chatbot_node
                           |
                  Tool Required?
                     /         \
                   Yes         No
                    |           |
                    v           v
                tool_node      END
                    |
                    v
              chatbot_node
                    |
                    v
                   END
                   
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
TAVILY_API_KEY=your_api_key_here
```

---

## 5. Run the backend 

```bash
uv run uvicorn app.main:app --reload
```

## 6. Run the frontend   

```
streamlit run .\frontend\app.py  
```

Open:

```
http://localhost:8501/
```

---

# 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

See the `LICENSE` file for more information.
