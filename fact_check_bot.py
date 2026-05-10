import os
import google.generativeai as genai
from tavily import TavilyClient

class FactCheckBot:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-3.1-flash-lite')
        
        self.tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def verify_claims(self, text):
        
        prompt = f"Identify 3 specific numerical or factual claims from this text. List them clearly. Text: {text[:4000]}"
        response = self.model.generate_content(prompt)
        claims = response.text.split('\n')
        
        results = []
        for claim in claims:
            if not claim.strip() or len(claim) < 10: continue
            
            
            search = self.tavily.search(query=claim, max_results=1)
            context = search['results'][0]['content'] if search['results'] else "No web data found."
            source_url = search['results'][0]['url'] if search['results'] else "No source"

            
            verify_prompt = f"""
            Claim from PDF: {claim}
            Web Evidence: {context}
            
            Is the PDF claim ✅ VERIFIED or ❌ FALSE? 
            Provide a 1-sentence explanation.
            """
            verdict_response = self.model.generate_content(verify_prompt)
            
            results.append({
                "claim": claim,
                "verdict": verdict_response.text,
                "source": source_url
            })
        return results