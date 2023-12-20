import requests
response = requests.get("https://www.otriviata.com/api.php?amount=10&type=boolean")
response.raise_for_status()
question_data = response.json()
