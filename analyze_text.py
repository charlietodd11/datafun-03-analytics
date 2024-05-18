import requests

# Fetching the text
url = 'https://shakespeare.mit.edu/hamlet/full.txt'
response = requests.get(url)
text = response.text.lower()

print(text)