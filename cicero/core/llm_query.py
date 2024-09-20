import requests
import os

class LLMClient:
    """
        Initialize the LLMClient.

        Parameters
        ----------
        mode: str
            'local' for using Ollama or 'external' for Groq.
        model: str
            The model to use for external calls (e.g., Groq).
        url: str
            The API URL for the local Ollama instance.
        api_key: str
            API key for external services (Groq).
        """
    def __init__(
        self,
        mode: str = None,
        model: str = None,
        url: str = None,
        api_key: str = None
    ):
        self.mode = mode
        self.model = model
        self.url = url
        self.api_key = api_key

        if mode == 'external':

            from groq import Groq
            assert api_key is not None, "You must provide and API Key"
            self.client = Groq(api_key=self.api_key)

    def query(self, prompt: str):
        """
        Make a query to the LLM.

        Parameters
        ----------
        prompt: str
            The text prompt to send to the model.
        
        Returns
        response: str
            The response from the model.
        """
        if self.mode == 'local':
            return self._query_local(prompt)
        elif self.mode == 'external':
            return self._query_external(prompt)
        
    def _query_local(self, prompt: str):
        """Handles local Ollama model queries."""
        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model, 
                    "prompt": prompt, 
                    "stream": False
                }
            )
            if response.status_code == 200:
                return response.json().get(
                    'response', 
                    'No response received from local model.'
                )
            else:
                return f"Error: Unable to get response, error code: {response.status_code}."
        except Exception as e:
            return f"Exception occurred during local query: {str(e)}"

    def _query_external(self, prompt: str):
        """Handles external Groq API queries."""
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.model
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Exception occurred during external query: {str(e)}"


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