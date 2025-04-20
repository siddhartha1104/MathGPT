"""
Wikipedia search tool.
"""

from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool

def create_wikipedia_tool():
    """
    Create and return a Wikipedia search tool.
    
    Returns:
        Tool: The Wikipedia search tool
    """
    wikipedia_wrapper = WikipediaAPIWrapper()
    
    return Tool(
        name="Wikipedia",
        func=wikipedia_wrapper.run,
        description="A tool for searching the Internet to find various information on the topics mentioned"
    )