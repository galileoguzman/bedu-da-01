import requests

response = requests.get('https://api.github.com')
# Print status code
print(response.status_code)
print(response.content)
