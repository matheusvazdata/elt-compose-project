from extract.api_client import fetch_data
from load.to_postgres import load_to_db

if __name__ == "__main__":
    data = fetch_data()
    load_to_db(data)