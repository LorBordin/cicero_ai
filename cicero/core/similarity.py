from cicero.templates.similarity import similarity_prompt
from sklearn.metrics.pairwise import cosine_similarity
import requests

def calculate_similarity(text1, text2, model):
    embedding1 = model.encode([text1])
    embedding2 = model.encode([text2])
    similarity = cosine_similarity(embedding1, embedding2)[0][0]
    return similarity


def calculate_similarity_llm(job_description, cv_text):
    prompt = similarity_prompt.format(job_description, cv_text)
    
    response = requests.post('http://localhost:11434/api/generate', 
                             json={
                                 "model": "llama3",
                                 "prompt": prompt,
                                 "stream": False
                             })
    
    if response.status_code == 200:
        return response.json()['response']
    else:
        return "Error: Unable to calculate similarities. Please ensure Ollama is running and Llama 3 is available."