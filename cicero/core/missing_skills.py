from cicero.templates.skills import missing_skills_prompt
import requests

def analyze_skills(job_description, cv_text):
    prompt = missing_skills_prompt.format(job_description, cv_text)

    response = requests.post('http://localhost:11434/api/generate', 
                             json={
                                 "model": "llama3",
                                 "prompt": prompt,
                                 "stream": False
                             })
    
    if response.status_code == 200:
        return response.json()['response']
    else:
        return "Error: Unable to analyze skills. Please ensure Ollama is running and Llama 3 is available."