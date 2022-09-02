from requests_oauthlib import OAuth1Session
import json
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
    x = len(fact)
    factpayload = fact[11:x-3]
else:
    print("Error:", response.status_code, response.text)


#Twitter automation portion starts here --

# API_KEY and API_SECRET
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# Adding our fact to the payload to tweet
payload = {"text": "⚡️ "+ factpayload+"."+" #Facts #MoreYouKnow"}

# Make the request to twitter
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Tweet success")

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
