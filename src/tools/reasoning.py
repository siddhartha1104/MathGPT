"""
Reasoning tool for mathematical problem-solving.
"""

from langchain.chains import LLMChain
from langchain.agents import Tool
from src.prompts.templates import get_reasoning_prompt_template

def create_reasoning_tool(llm):
    """
    Create and return a reasoning tool.
    
    Args:
        llm: The language model to use for reasoning
        
    Returns:
        Tool: The reasoning tool
    """
    prompt_template = get_reasoning_prompt_template()
    chain = LLMChain(llm=llm, prompt=prompt_template)
    
    return Tool(
        name="Reasoning tool",
        func=chain.run,
        description="A tool for answering logic-based and reasoning questions."
    )