# MathGPT

## Overview

MathGPT is an advanced chatbot designed to solve both basic and complex mathematical problems. It leverages AI technology to provide step-by-step solutions and explanations for a wide range of mathematical concepts and problems.

## Features

- Solves arithmetic, algebra, calculus, statistics, and more
- Provides detailed step-by-step solutions
- Offers explanations of mathematical concepts
- Handles complex equations and problems
- Maintains conversation history for contextual problem-solving

## Project Structure

```
MathGPT/
│
├── app.py                # Main Streamlit application entry point
├── .env                  # Environment variables (API keys)
├── .gitignore            # Git ignore file
├── requirements.txt      # Project dependencies
│
├── config/
│   └── settings.py       # Configuration settings
│
├── src/
│   ├── __init__.py
│   ├── agent/
│   │   ├── __init__.py
│   │   └── math_agent.py # Agent initialization and configuration
│   │
│   ├── llm/
│   │   ├── __init__.py
│   │   └── model.py      # LLM initialization
│   │
│   ├── memory/
│   │   ├── __init__.py
│   │   └── chat_memory.py # Memory management
│   │
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── templates.py   # Prompt templates
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── calculator.py  # Math calculation tools
│   │   ├── wikipedia.py   # Wikipedia search tools
│   │   └── reasoning.py   # Reasoning chain tools
│   │
│   └── ui/
│       ├── __init__.py
│       └── components.py  # UI components and functions
│
└── tests/
    ├── __init__.py
    ├── test_agent.py
    ├── test_tools.py
    └── test_memory.py
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Groq API key

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/siddhartha1104/MathGPT.git
   cd MathGPT
   ```

2. Create and activate a virtual environment:

   ```bash
   conda create -p venv python==3.11 -y
   conda activate venv/ # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Get your API key:

   - Go to the Groq website (https://groq.com)
   - Create an account
   - Navigate to the API section to generate your API key

5. Create `.env` file (see project structure aboove) with your API key:
   ```
   LLM_API_KEY=your_groq_api_key_here
   ```

## Usage

### Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will be available at http://localhost:8501 in your web browser.

### Example Interactions

You can ask MathGPT various types of math questions:

- "Solve the quadratic equation: 2x² + 5x - 3 = 0"
- "What is the derivative of f(x) = x³ + 2x² - 5x + 7?"
- "Calculate the probability of drawing 3 red cards in a row from a standard deck without replacement"
- "Help me understand the concept of integration by parts"

## Contact

For questions or suggestions, please open an issue on the GitHub repository.

--
mail@siddharthapathak.com.np
