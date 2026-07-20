from langgraph.prebuilt import ToolNode

from src.llm.llm_model import llm_model

from src.tools.calculator import calculator
from src.tools.rag_tool import rag_tool
from src.tools.web_search import web_search


tools = [
    calculator,
    
    rag_tool,

    web_search
]


tool_node = ToolNode(tools)


agent_llm = llm_model.bind_tools(tools) # type: ignore