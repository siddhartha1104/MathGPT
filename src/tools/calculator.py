"""
Calculator tool for math operations.
"""

from langchain.chains import LLMMathChain
from langchain.agents import Tool

def create_calculator_tool(llm):
    """
    Create and return a calculator tool.
    
    Args:
        llm: The language model to use for the calculator
        
    Returns:
        Tool: The calculator tool
    """
    math_chain = LLMMathChain.from_llm(llm=llm)
    
    return Tool(
        name="Calculator",
        func=math_chain.run,
        description="A tool for answering math related questions. Only input mathematical expression need to be provided"
    )