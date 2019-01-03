# Anti-Swear Bot
Parses reddit comments for light profanity and replies with a message reminding the user to watch their language. The comment will also provide a count of repeat offenses.

# Prerequisites
1. `sudo pip3 install praw`
	Praw is the Python Reddit API wrapper. It is the only API in this project that is being used to connect and manipulate data from Reddit

# Installing and configuring
The only configuration required to run this bot is to create a `config.py` file. Reddit API details must be filled in here. Please follow the steps below:

```
git clone https://github.com/sathusank/saintredditbot
cd src
mv example.config.py config.py
nano config.py
```

# Deployment
run `main.py`
