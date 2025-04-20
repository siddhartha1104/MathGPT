import streamlit as st
from dotenv import load_dotenv

# Local imports
from src.llm.model import initialize_llm
from src.agent.math_agent import create_math_agent
from src.memory.chat_memory import initialize_memory
from src.ui.components import (
    setup_page_config,
    display_chat_history,
    display_memory_debug,
    handle_clear_history,
    create_sidebar_options,
    display_footer
)

# Load environment variables from .env file
load_dotenv()

def main():
    # Set up the Streamlit app
    setup_page_config()
    
    # Initialize the LLM
    llm = initialize_llm()
    
    # Initialize memory system
    memory, msgs = initialize_memory()
    
    # Create the math agent
    assistant_agent = create_math_agent(llm, memory)
    
    # Create sidebar options
    create_sidebar_options()
    
    # Display chat history
    display_chat_history(msgs)
    
    # Add a clear chat button in the sidebar
    handle_clear_history(msgs)
    
    # Add a sidebar option to display conversation memory
    display_memory_debug(memory)
    
    # Set up layout for better chat experience
    chat_container = st.container()
    
    # Chat input handling
    if prompt := st.chat_input("Ask me a math problem...", key="chat_input"):
        # Add user message to chat history for display
        st.session_state.ui_messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Store in LangChain's memory
        msgs.add_user_message(prompt)
        
        # Display assistant response in chat container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Thinking...")
            
            # Create a container for the callback handler
            callback_container = st.container()
            
            # Process the user's input
            with st.spinner("Solving your math problem..."):
                from langchain.callbacks import StreamlitCallbackHandler
                st_cb = StreamlitCallbackHandler(callback_container, expand_new_thoughts=False)
                
                try:
                    # Run the agent with input
                    response = assistant_agent.run(input=prompt, callbacks=[st_cb])
                    message_placeholder.markdown(response)
                    
                    # Add assistant response to both UI messages and LangChain memory
                    st.session_state.ui_messages.append({"role": "assistant", "content": response})
                    msgs.add_ai_message(response)
                    
                    # Optional: Extract and store mathematical concepts for enhanced memory
                    # This would call a function to parse the response for math concepts
                    
                except Exception as e:
                    error_message = f"An error occurred: {str(e)}"
                    message_placeholder.markdown(error_message)
                    st.session_state.ui_messages.append({"role": "assistant", "content": error_message})
                    msgs.add_ai_message(error_message)
    
    # Add a small footer
    display_footer()

if __name__ == "__main__":
    main()