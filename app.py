import streamlit as st
from PyPDF2 import PdfReader
from fact_check_bot import FactCheckBot
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="TruthLayer Agent", page_icon="🛡️")
st.title("🛡️ TruthLayer: Fact-Check Agent")

uploaded_file = st.file_uploader("Upload Marketing PDF", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = "".join([page.extract_text() for page in reader.pages])
    
    if st.button("Start Automated Factchecking"):
        if not os.getenv("GEMINI_API_KEY") or not os.getenv("TAVILY_API_KEY"):
            st.error("API Keys missing! Check your .env file or Streamlit Secrets.")
        else:
            bot = FactCheckBot()
            with st.spinner("🔍 Checking claims against live web data..."):
                results = bot.verify_claims(text)
                for res in results:
                    with st.expander(f"Analysis: {res['claim'][:60]}..."):
                        st.write(res['verdict'])
                        st.caption(f"Source: {res['source']}")