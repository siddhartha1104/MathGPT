"""
Enhanced memory management for mathematical context retention.
"""

import streamlit as st
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from config.settings import MEMORY_KEY, WELCOME_MESSAGE, MEMORY_WINDOW_SIZE

class MathContextMemory:
    """Extended memory class that manages mathematical context appropriately."""
    
    def __init__(self, memory_key=MEMORY_KEY):
        """Initialize the math context memory system."""
        self.msgs = StreamlitChatMessageHistory(key=memory_key)
        
        # Use window memory to keep relevant context but prevent token overflow
        self.memory = ConversationBufferWindowMemory(
            memory_key="chat_history",
            chat_memory=self.msgs,
            return_messages=True,
            output_key="output",
            k=MEMORY_WINDOW_SIZE  # Keep last N interactions
        )
        
        # Track important mathematical concepts mentioned
        self.math_concepts = set()
        self.variables = {}
        self.equations = []
    
    def extract_math_context(self, message):
        """Extract important mathematical context from messages."""
        # This could be enhanced with regex patterns to identify equations,
        # variables, and math concepts for persistent storage beyond window size
        # For now, this is a placeholder for the concept
        pass
    
    def prune_irrelevant_context(self):
        """Remove irrelevant context to keep focus on current math problem."""
        # This would implement heuristics to determine relevant vs. irrelevant math context
        # For now, this is a placeholder for the concept
        pass
    
    def get_memory(self):
        """Get the memory object for the agent."""
        return self.memory
    
    def get_message_history(self):
        """Get the message history object."""
        return self.msgs

def initialize_memory():
    """
    Initialize and return enhanced memory components for math problem solving.
    
    Returns:
        tuple: (memory, message_history)
    """
    # Create the enhanced math context memory
    math_memory = MathContextMemory()
    memory = math_memory.get_memory()
    msgs = math_memory.get_message_history()
    
    # Set up UI for messages
    if "ui_messages" not in st.session_state:
        st.session_state.ui_messages = []
        # Add a welcome message if it's the first time
        if not msgs.messages:
            st.session_state.ui_messages.append({"role": "assistant", "content": WELCOME_MESSAGE})
            msgs.add_ai_message(WELCOME_MESSAGE)
    
    return memory, msgs