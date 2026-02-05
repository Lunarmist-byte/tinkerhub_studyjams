import requests
def get_random_jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Setup:", data.get("setup", "No setup found"))
    print("Punchline:", data.get("punchline", "No punchline found"))
get_random_jokes()
