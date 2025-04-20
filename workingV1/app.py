import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain, ConversationChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory

# Load environment variables from .env file
load_dotenv()

# Set up the Streamlit app
st.set_page_config(page_title="Math Problem Solver Assistant", page_icon="🧮")
st.title("Math Problem Solver Using Google Gemma 2")

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("Error: GROQ_API_KEY is not set in the .env file. Please contact the administrator.")
    st.stop()

# Initialize the model
llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Initialize chat message history
msgs = StreamlitChatMessageHistory(key="chat_messages")

# Initialize memory with a longer history capacity
memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=msgs,
    return_messages=True,
    output_key="output"  # Explicitly specify output key
)

# Initialize tools
wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the Internet to find various information on the topics mentioned"
)

math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for answering math related questions. Only input mathematical expression need to be provided"
)

# Create a system prompt that emphasizes context retention
prompt = """
You're an agent specialized in solving mathematical questions. Please use your knowledge and the tools available to provide detailed solutions.

Always refer to our previous conversation when context is important. Remember details from our earlier exchanges to provide consistent and contextually relevant responses.

For the current question: {question}

Think step by step, show your reasoning, and provide a clear explanation.
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

chain = LLMChain(llm=llm, prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

# Enhanced agent prompt that emphasizes remembering context
system_message = """You are a helpful AI math assistant that remembers our entire conversation history.
When answering new questions, refer to our previous exchanges when relevant. 
If the user refers to something we discussed earlier, use that context in your response."""

# Initialize the agent with memory and enhanced system message
assistant_agent = initialize_agent(
    tools=[wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True,
    memory=memory,
    agent_kwargs={
        "system_message": system_message
    }
)

# Set up UI for messages
if "ui_messages" not in st.session_state:
    st.session_state.ui_messages = []
    # Add a welcome message if it's the first time
    if not msgs.messages:
        welcome_msg = "Hi, I'm a Math chatbot who can answer all your math questions. How can I help you today?"
        st.session_state.ui_messages.append({"role": "assistant", "content": welcome_msg})
        msgs.add_ai_message(welcome_msg)

# Display chat messages from history on app rerun
for message in st.session_state.ui_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Add a clear chat button in the sidebar
if st.sidebar.button("Clear Chat History"):
    msgs.clear()
    st.session_state.ui_messages = []
    welcome_msg = "Chat history cleared. How can I help you today?"
    st.session_state.ui_messages.append({"role": "assistant", "content": welcome_msg})
    msgs.add_ai_message(welcome_msg)
    st.rerun()

# Add a sidebar option to display conversation memory
if st.sidebar.checkbox("Show Conversation Memory"):
    st.sidebar.subheader("Current Conversation Memory")
    memory_container = st.sidebar.container()
    memory_messages = memory.chat_memory.messages
    for i, msg in enumerate(memory_messages):
        memory_container.text(f"{msg.type}: {msg.content[:50]}..." if len(msg.content) > 50 else f"{msg.type}: {msg.content}")

# Chat input at the bottom of the page
if prompt := st.chat_input("Ask me a math question..."):
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
        with st.spinner(""):
            st_cb = StreamlitCallbackHandler(callback_container, expand_new_thoughts=False)
            
            try:
                # Run the agent with input
                response = assistant_agent.run(input=prompt, callbacks=[st_cb])
                message_placeholder.markdown(response)
                
                # Add assistant response to both UI messages and LangChain memory
                st.session_state.ui_messages.append({"role": "assistant", "content": response})
                msgs.add_ai_message(response)
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                message_placeholder.markdown(error_message)
                st.session_state.ui_messages.append({"role": "assistant", "content": error_message})
                msgs.add_ai_message(error_message)

# Add a small footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray; font-size: 0.8em;'>Developed by Siddhartha Pathak</div>", unsafe_allow_html=True)