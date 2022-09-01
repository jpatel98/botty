import requests
import os

#retrieving API Ninja key from environment using os
API_NINJA_KEY = os.environ.get("API_NINJA_KEY")

#making an API call to retrieve a random fact
limit = 1
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': API_NINJA_KEY})
#If response is ok, print the text
if response.status_code == requests.codes.ok:
    fact = response.text
    print(fact)
else:
    print("Error:", response.status_code, response.text)

