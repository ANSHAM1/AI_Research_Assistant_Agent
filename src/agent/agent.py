from langgraph.prebuilt import ToolNode

from src.llm.llm_model import llm_model

from src.tools.calculator import calculator
from src.tools.search import search


tools = [
    calculator,

    search
]


tool_node = ToolNode(tools)


agent_llm = llm_model.bind_tools(tools) # type: ignore