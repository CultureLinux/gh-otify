# gh-otify

<p align="center">
  <img src="https://github.com/CultureLinux/gh-otify/blob/develop/images/gh-otify.png" alt="gh-otify"/>
</p>

This script monitors GitHub repositories for new tags or releases and sends notifications via Discord or Bluesky.

## Features

- Automatically tracks GitHub tags for a specified list of repositories.
- Notifications:
  - **Discord**: Sends messages to a specific channel.
  - **Bluesky (Bsky)**: Posts notifications to a Bluesky account.
- Keeps track of previously detected tags to avoid duplicate notifications.

## Prerequisites

- **Python 3.9 or higher**
- A GitHub token to access the GitHub API.
- A Discord account (with a bot and a configured channel if using Discord notifications).
- A Bluesky account (if using Bluesky notifications).

## Install 
### Os packages
    dnf install python3-dotenv
### Python packages
    git clone https://github.com/CultureLinux/gh-otify.git
    cd gh-otify
    python -m venv venv
    source venv/bin/activate
    pip install -r requierements.txt
    cp .env_default .env

## Env files

Adapt on your needs

### Github token
Create your token here [Github](https://github.com/settings/tokens) to get a better api rate limit

### Discord notification
Create your bot by following instructions here [Discord](https://docs.discordbotstudio.org/setting-up-dbs/finding-your-bot-token)

### Bsky notification
Use your handle and password
