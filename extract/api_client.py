import requests

def fetch_data():
    print("🔄 Buscando dados da API...")
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    return response.json()