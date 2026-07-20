from langgraph.prebuilt import ToolNode

from src.llm.model import llm

from src.tools.calculator import calculator
from src.tools.rag_tool import rag_tool
from src.tools.web_search import web_search


tools = [
    calculator,
    
    rag_tool,

    web_search
]


tool_node = ToolNode(tools)


agent_llm = llm.bind_tools(tools) # type: ignore