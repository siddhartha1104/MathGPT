"""
Enhanced configuration settings for the Math Problem Solver application.
"""

import os

# Model settings
LLM_MODEL = "Gemma2-9b-It"  # Consider using a more powerful model if available
LLM_TEMPERATURE = 0.2  # Lower temperature for more precise math reasoning
MAX_TOKENS = 4096  # Ensure enough tokens for complex explanations

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Application settings
APP_TITLE = "Advanced Math Problem Solver"
APP_ICON = "🧮"
VERBOSE_AGENT = False  # Set to True to see agent's reasoning process

# Memory settings
MEMORY_KEY = "chat_messages"
MEMORY_WINDOW_SIZE = 10  # Number of conversation turns to keep in memory

# Welcome message
WELCOME_MESSAGE = """Hi, I'm an Advanced Math Problem Solver that can help with everything from basic arithmetic to calculus, linear algebra, statistics, and more.

I can:
- Solve step-by-step math problems 
- Remember our previous work and refer back to it
- Handle complex, multi-step problems
- Explain mathematical concepts

What math problem can I help you with today?"""

CLEAR_HISTORY_MESSAGE = "Chat history cleared. What math problem can I help you with today?"

# Footer info
FOOTER_TEXT = "Developed by Siddhartha Pathak | Enhanced Math Edition"

# Math domains supported
SUPPORTED_MATH_DOMAINS = [
    "Arithmetic",
    "Algebra",
    "Geometry",
    "Trigonometry",
    "Calculus",
    "Linear Algebra",
    "Differential Equations",
    "Statistics",
    "Probability",
    "Number Theory",
    "Graph Theory",
    "Optimization"
]