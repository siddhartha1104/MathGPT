"""
Enhanced UI components for the Streamlit application.
"""

import streamlit as st
from config.settings import APP_TITLE, APP_ICON, CLEAR_HISTORY_MESSAGE, FOOTER_TEXT, SUPPORTED_MATH_DOMAINS

def setup_page_config():
    """Set up the page configuration for Streamlit."""
    st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide")
    st.title(APP_TITLE)

def display_chat_history(msgs):
    """
    Display chat message history in the UI.
    
    Args:
        msgs: The message history object
    """
    # Display chat messages from history on app rerun
    for message in st.session_state.ui_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def create_sidebar_options():
    """Create enhanced sidebar options for the app."""
    st.sidebar.title("Options & Settings")
    
    # Math domain information
    with st.sidebar.expander("Supported Math Domains"):
        st.write("This solver can handle problems from these domains:")
        for domain in SUPPORTED_MATH_DOMAINS:
            st.write(f"- {domain}")
    
    # Example problems
    with st.sidebar.expander("Example Problems"):
        st.write("Try asking about:")
        st.write("- Solve the quadratic equation: 2x² + 5x - 3 = 0")
        st.write("- Find the derivative of f(x) = x³ - 4x² + 7x - 9")
        st.write("- Calculate the eigenvalues of matrix [[4, 2], [1, 3]]")
        st.write("- What's the probability of getting at least 2 heads in 5 coin flips?")
    
    # Math cheat sheet
    with st.sidebar.expander("Math Formula Cheat Sheet"):
        st.write("**Quadratic Formula**")
        st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        
        st.write("**Derivative Rules**")
        st.latex(r"\frac{d}{dx}(x^n) = nx^{n-1}")
        
        st.write("**Integration Rules**")
        st.latex(r"\int x^n dx = \frac{x^{n+1}}{n+1} + C, n \neq -1")

def handle_clear_history(msgs):
    """
    Handle clearing the chat history.
    
    Args:
        msgs: The message history object
    """
    if st.sidebar.button("Clear Chat History"):
        msgs.clear()
        st.session_state.ui_messages = []
        welcome_msg = CLEAR_HISTORY_MESSAGE
        st.session_state.ui_messages.append({"role": "assistant", "content": welcome_msg})
        msgs.add_ai_message(welcome_msg)
        st.rerun()

def display_memory_debug(memory):
    """
    Display enhanced memory debugging information in the sidebar.
    
    Args:
        memory: The memory object to debug
    """
    if st.sidebar.checkbox("Show Conversation Memory"):
        st.sidebar.subheader("Current Conversation Memory")
        memory_container = st.sidebar.container()
        memory_messages = memory.chat_memory.messages
        
        # Create tabs for different memory views
        tab1, tab2 = st.sidebar.tabs(["Message History", "Math Context"])
        
        with tab1:
            for i, msg in enumerate(memory_messages):
                is_important = "✓" if i >= len(memory_messages) - 4 else ""  # Mark recent messages
                memory_container.text(
                    f"{is_important} {msg.type}: {msg.content[:40]}..." 
                    if len(msg.content) > 40 
                    else f"{is_important} {msg.type}: {msg.content}"
                )
        
        with tab2:
            # This would display mathematical context extracted from the conversation
            # Such as tracked variables, equations, and concepts
            st.write("Math context tracking would appear here")
            st.write("(Variables, equations, theorems referenced, etc.)")

def display_footer():
    """Display the enhanced footer for the application."""
    st.markdown("---")
    footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])
    with footer_col2:
        st.markdown(
            f"<div style='text-align: center; color: gray; font-size: 0.8em;'>{FOOTER_TEXT}</div>", 
            unsafe_allow_html=True
        )