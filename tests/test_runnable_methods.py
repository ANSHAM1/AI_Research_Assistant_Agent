from src.rag.chain import rag_chain


question = "Explain vector databases"


print("NORMAL")
print(
    rag_chain.invoke(question)
)


print("\nSTREAM")


for chunk in rag_chain.stream(question):
    print(chunk)