import requests

def llm_query(
    prompt: str,
    api_url: str = 'http://localhost:11434/api/generate',
    model: str = "llama3"
):
    response = requests.post(
        api_url, 
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    if response.status_code == 200:
        return response.json()['response']
    else:
        return f"Error: Unable to get response, erro code: {response.status_code}."