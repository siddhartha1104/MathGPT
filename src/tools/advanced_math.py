"""
Advanced mathematical tools for complex problem solving.
"""

from langchain.agents import Tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def create_calculus_tool(llm):
    """
    Create a specialized tool for calculus problems.
    
    Args:
        llm: The language model to use
        
    Returns:
        Tool: The calculus tool
    """
    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        You are a calculus expert. Solve the following calculus problem step by step:
        
        Problem: {question}
        
        Show your work in detail:
        1. Identify what type of calculus problem this is (differentiation, integration, etc.)
        2. List any relevant formulas or theorems
        3. Show each step of your solution with explanations
        4. Check your answer if possible
        """
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    return Tool(
        name="Calculus",
        func=chain.run,
        description="Solves calculus problems including derivatives, integrals, limits, series, and differential equations."
    )

def create_linear_algebra_tool(llm):
    """
    Create a specialized tool for linear algebra problems.
    
    Args:
        llm: The language model to use
        
    Returns:
        Tool: The linear algebra tool
    """
    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        You are a linear algebra expert. Solve the following linear algebra problem step by step:
        
        Problem: {question}
        
        Show your work in detail:
        1. Identify what type of linear algebra problem this is (matrix operations, eigenvalues, etc.)
        2. List any relevant formulas or theorems
        3. Show each step of your solution with explanations
        4. Check your answer if possible
        """
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    return Tool(
        name="LinearAlgebra",
        func=chain.run,
        description="Solves linear algebra problems including matrices, determinants, eigenvalues, vector spaces, and transformations."
    )

def create_statistics_tool(llm):
    """
    Create a specialized tool for statistics problems.
    
    Args:
        llm: The language model to use
        
    Returns:
        Tool: The statistics tool
    """
    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        You are a statistics expert. Solve the following statistics problem step by step:
        
        Problem: {question}
        
        Show your work in detail:
        1. Identify what type of statistics problem this is (probability, hypothesis testing, etc.)
        2. List any relevant formulas or theorems
        3. Show each step of your solution with explanations
        4. Check your answer if possible
        """
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    return Tool(
        name="Statistics",
        func=chain.run,
        description="Solves statistics problems including probability, distributions, hypothesis testing, confidence intervals, and regression analysis."
    )

def create_chain_of_thought_tool(llm):
    """
    Create a tool that breaks down complex math problems using chain-of-thought reasoning.
    
    Args:
        llm: The language model to use
        
    Returns:
        Tool: The chain-of-thought tool
    """
    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        You are an expert mathematician who excels at breaking down complex problems.
        
        Problem: {question}
        
        Think step by step:
        1. What's the core concept being tested here?
        2. Break the problem into smaller sub-problems
        3. Solve each sub-problem methodically
        4. Combine the results to find the final answer
        5. Verify the solution makes sense
        
        Provide your complete thought process and final answer.
        """
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    return Tool(
        name="ComplexProblemSolver",
        func=chain.run,
        description="Breaks down any complex mathematical problem into manageable steps and solves it methodically."
    )