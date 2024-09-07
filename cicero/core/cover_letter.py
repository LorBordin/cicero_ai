from cicero.templates.cover_letter import cover_letter_prompt
import requests

def generate_cover_letter(job_description, cv_text):
    prompt = cover_letter_prompt.format(job_description, cv_text)

    response = requests.post('http://localhost:11434/api/generate', 
                             json={
                                 "model": "llama3",
                                 "prompt": prompt,
                                 "stream": False
                             })
    
    if response.status_code == 200:
        return response.json()['response']
    else:
        return "Error: Unable to generate cover letter. Please ensure Ollama is running and Llama 3 is available."