import requests
import os

class LLMClient:
    """
        Initialize the LLMClient.

        Parameters
        ----------
        client: str
            'ollama' for using Ollama local or 'groq' for Groq.
        model: str
            The model to use for external calls (e.g., Groq).
        url: str
            The API URL for the local Ollama instance.
        api_key: str
            API key for external services (Groq).
        """
    def __init__(
        self,
        client_name: str = None,
        model: str = None,
        url: str = None,
        api_key: str = None
    ):
        self.client_name = client_name
        self.model = model
        self.url = url
        self.api_key = api_key

        if client_name == 'groq':

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
        if self.client_name == 'ollama':
            return self._query_local(prompt)
        elif self.client_name == 'groq':
            return self._query_external(prompt)
        else:
            print(f"Unrecognized client: {self.client_name}")

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