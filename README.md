
# Botty Twitter Bot
[Botty](https://twitter.com/factzbot) is a Twitter Bot that Tweets random facts hourly. 
It is built using the [manage Tweets ](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/introduction)endpoint in the Twitter API v2 and deployed with [Pythonanywhere](https://www.pythonanywhere.com/). 
This bot parses random facts from an API that provides random facts, [api-ninjas](https://api-ninjas.com/), and Tweets them out.

## Tech Used

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

[![v2](https://img.shields.io/endpoint?url=https%3A%2F%2Ftwbadges.glitch.me%2Fbadges%2Fv2)](https://developer.twitter.com/en/docs/twitter-api)


## Environment Variables

To locally run this project, you will need to add the following environment variables to your local python environment. 

API-ninja key: `API_NINJA_KEY`

Twitter keys: `CONSUMER_KEY` `CONSUMER_SECRET` `ACCESS_TOKEN` `ACCESS_TOKEN_SECRET`


- ### Steps acquire the keys and tokens
    - You will be required to sign up for an api key from [api-ninja.](https://api-ninjas.com/)
    - You will need to create a [new twitter account](http://twitter.com/signup) for your bot.
    - Before you can use the Twitter API v2, you will need a [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info). You can learn more about getting started with the Twitter API in the [getting started](https://developer.twitter.com/en/docs/getting-started) section of the documentation. 

## Run Locally

Clone the project

```bash
git clone git@github.com:jpatel98/botty.git
```

Go to the project directory

```bash
cd botty
```

Install requirememnts

```bash
pip install -r requirements.txt
```
Set the environment variables

```bash
export "API_NINJA_KEY"="<your key>"
export "CONSUMER_KEY"="<your key>"
export "CONSUMER_SECRET"="<your key>"
export "ACCESS_TOKEN"="<your key>"
export "ACCESS_TOKEN_SECRET"="<your key>"
```
Start the app

```bash
python bot.py
```
## Deployment
The bot has been deployed and scheduled to run hourly using [Pythonanywhere](https://www.pythonanywhere.com/).

You can check the live bot at - https://twitter.com/factzbot 
