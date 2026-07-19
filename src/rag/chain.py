from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (RunnableLambda, RunnablePassthrough)

from src.llm.model import llm
from src.rag.vectorstore import retriever

rag_prompt = ChatPromptTemplate.from_template(
    """
You are ResearchMind AI.

You are an intelligent research assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
clearly say that the information is not available.

------------------------

Context:

{context}

------------------------

Question:

{question}

Answer:
"""
)

output_parser = StrOutputParser()

def format_documents(documents : list[Document]) -> str:
    return "\n\n".join(document.page_content for document in documents)

rag_chain = (
    {
        "context": retriever | RunnableLambda(format_documents),
        "question": RunnablePassthrough()
    }

    | rag_prompt 
    
    | llm 
    
    | output_parser
)

def generate_answer(question: str) -> str:
    return rag_chain.invoke(question)

# def generate_answer(question: str) -> str:
#     documents = retriever.invoke(question)

#     context = format_documents(documents)

#     prompt = rag_prompt.invoke(
#         {
#             "context": context,

#             "question": question,
#         }
#     )

#     response = llm.invoke(prompt)

#     return output_parser.invoke(response)