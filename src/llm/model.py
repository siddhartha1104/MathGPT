"""
Enhanced language model initialization with better math capabilities.
"""

import os
import streamlit as st
from langchain_groq import ChatGroq
from config.settings import LLM_MODEL, GROQ_API_KEY, LLM_TEMPERATURE

def initialize_llm():
    """
    Initialize and return the language model optimized for mathematical reasoning.
    
    Returns:
        The initialized language model object with optimal math settings
    """
    # Verify API key is available
    if not GROQ_API_KEY:
        st.error("Error: GROQ_API_KEY is not set in the .env file. Please contact the administrator.")
        st.stop()
    
    # Initialize the model with settings optimized for mathematical reasoning
    # Lower temperature for more precise mathematical calculations
    llm = ChatGroq(
        model=LLM_MODEL, 
        groq_api_key=GROQ_API_KEY,
        temperature=LLM_TEMPERATURE,
        max_tokens=4096  # Ensure longer responses for complex math explanations
    )
    
    return llm