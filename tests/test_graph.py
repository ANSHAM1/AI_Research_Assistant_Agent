from src.graph.workflow import rag_graph



result = rag_graph.invoke(  # type: ignore
    {
        "question":
        "Give my Name",

        "documents":[],

        "answer":""
    }
)


print(result["answer"])