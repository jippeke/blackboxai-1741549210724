import requests
import json

class KVKAPIClient:
    def __init__(self, api_key, test_environment=True):
        """
        Initialize the KVK API client
        
        Args:
            api_key (str): Your KVK API key
            test_environment (bool): Use test environment if True
        """
        self.api_key = api_key
        self.base_url = "https://api.kvk.nl/test/api/v1" if test_environment else "https://api.kvk.nl/api/v1"
        self.headers = {
            "apikey": self.api_key,
            "Accept": "application/json"
        }

    def search_company(self, kvk_number):
        """
        Search for company information using KVK number
        
        Args:
            kvk_number (str): The KVK number to search for
            
        Returns:
            dict: Company information or error details
        """
        endpoint = f"{self.base_url}/basisprofielen/{kvk_number}"
        
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

def main():
    # Replace with your actual KVK API key
    api_key = "YOUR_API_KEY_HERE"
    
    # Initialize the client
    client = KVKAPIClient(api_key, test_environment=True)
    
    # Example KVK number (use test numbers from KVK documentation)
    kvk_number = "90004760"  # Example test KVK number
    
    # Search for company information
    result = client.search_company(kvk_number)
    
    # Print the result
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
