TruthLayer: AI-Powered Fact-Check Agent
TruthLayer is an intelligent fact-checking assistant designed to verify claims within PDF documents. By leveraging Google Gemini's reasoning capabilities and Tavily's real-time search API, the agent identifies key claims and cross-references them with live web data to determine their accuracy.

🚀 Features
PDF Analysis: Extracts and processes text from uploaded documents.

Automated Claim Extraction: Uses LLMs to identify verifiable statements.

Real-time Verification: Integrated with Tavily Search API for up-to-the-minute web grounding.

Verdict Generation: Provides a "Fact", "Partial", or "False" verdict with supporting evidence.

🛠️ Technical Stack
Frontend: Streamlit

LLM: Google Gemini 1.5 Flash

Search Engine: Tavily AI

Language: Python 3.10+

⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/Harshit-py13/fact-check-agent.git
cd fact-check-agent
Install dependencies:

Bash
pip install -r requirements.txt
Environment Variables:
Create a .env file or set Streamlit Secrets with:

Plaintext
GEMINI_API_KEY = "your_google_api_key"
TAVILY_API_KEY = "your_tavily_api_key"
Run the App:

Bash
streamlit run app.py
