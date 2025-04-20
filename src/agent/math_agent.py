"""
Enhanced math problem solving agent configuration.
"""

from langchain.agents.agent_types import AgentType
from langchain.agents import initialize_agent, AgentExecutor, load_tools
from src.tools.calculator import create_calculator_tool
from src.tools.wikipedia import create_wikipedia_tool
from src.tools.reasoning import create_reasoning_tool
from src.tools.advanced_math import (
    create_calculus_tool,
    create_linear_algebra_tool, 
    create_statistics_tool,
    create_chain_of_thought_tool
)
from src.prompts.templates import get_system_message
from config.settings import VERBOSE_AGENT

def create_math_agent(llm, memory):
    """
    Create and return an enhanced math problem solving agent.
    
    Args:
        llm: The language model to use for the agent
        memory: The memory system for the agent
        
    Returns:
        Agent: The initialized math problem solving agent
    """
    # Initialize standard tools
    calculator_tool = create_calculator_tool(llm)
    wikipedia_tool = create_wikipedia_tool()
    reasoning_tool = create_reasoning_tool(llm)
    
    # Initialize advanced math tools
    calculus_tool = create_calculus_tool(llm)
    linear_algebra_tool = create_linear_algebra_tool(llm)
    statistics_tool = create_statistics_tool(llm)
    cot_tool = create_chain_of_thought_tool(llm)
    
    # Additional LangChain tools that might be useful
    additional_tools = load_tools(
        ["llm-math"],
        llm=llm
    )
    
    # Compile all tools
    all_tools = [
        calculator_tool, 
        wikipedia_tool, 
        reasoning_tool,
        calculus_tool,
        linear_algebra_tool,
        statistics_tool,
        cot_tool,
        *additional_tools
    ]
    
    # Get system message
    system_message = get_system_message()
    
    # Initialize the agent with memory and enhanced system message
    agent = initialize_agent(
        tools=all_tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=VERBOSE_AGENT,
        handle_parsing_errors=True,
        memory=memory,
        agent_kwargs={
            "system_message": system_message
        },
        max_iterations=6,  # Allow more iterations for complex math problems
        early_stopping_method="generate"  # Better handling of complex reasoning
    )
    
    return agent