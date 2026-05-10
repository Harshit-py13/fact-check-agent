Fact Check Agent
An AI-powered fact-checking tool that verifies claims from URLs or text input using CrewAI and OpenAI's GPT-4.

Features
URL fact-checking: Analyze articles and extract verifiable claims
Text fact-checking: Process direct text input for claim verification
Specialized handling for news sources (e.g., BBC)
Multi-agent system using CrewAI for thorough fact verification
Advanced web scraping with Firecrawl and fallback mechanisms
DuckDuckGo search integration for claim verification
Beautiful Streamlit interface
Setup
Clone the repository
Create a virtual environment:
python -m venv env
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Create a .env file with your API keys:
GEMINI_API_KEY = "your_key"
TAVILY_API_KEY = "your_key"
⚠️ Security Note: Never commit your .env file or expose your API keys. The .gitignore file is configured to exclude sensitive files.

Usage
Run the Streamlit app:

python -m streamlit run app.py
The app will be available at http://localhost:8501

Components
app.py: Main Streamlit interface
fact_check_bot.py: Core fact-checking logic and CrewAI implementation
Agents:
Content Extractor: Scrapes and cleans webpage content
Claim Identifier: Extracts verifiable claims
Fact Researcher: Gathers evidence using DuckDuckGo search
Claim Verifier: Analyzes claims against evidence
Credibility Summarizer: Provides final analysis
Input Methods
URL Input:

Paste a news article URL
Click "Check Credibility"
View extracted claims and verification results
Text Input:

Enter text directly
Click "Check Text"
View claims and verification results
Tests
Run the test suite with:

python -m pytest tests/
The tests cover:

Basic functionality
Credibility rating extraction
Error handling for missing API keys
Requirements
Key dependencies (see requirements.txt for full list):

Python 3.8+
streamlit >= 1.31.0
crewai >= 0.16.2
openai >= 1.12.0
langchain >= 0.1.0
duckduckgo-search >= 7.5.2
firecrawl >= 0.1.0 (optional)
beautifulsoup4 >= 4.12.0
python-dotenv >= 1.0.0
Security Best Practices
API Keys:

Store API keys in environment variables
Never hardcode sensitive information
Use .env file for local development
For production, use secure secret management
Input Validation:

All URLs are validated and sanitized
Text input is cleaned and validated
Error handling for malformed inputs
Dependencies:

Keep dependencies updated
Run pip install --upgrade periodically
Check for security vulnerabilities
Error Handling:

Proper error messages without exposing system details
Graceful fallback mechanisms
Comprehensive logging without sensitive information
