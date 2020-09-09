# Hack the Remote

Collab: Elastic Spaces<br>
Fall 2020<br>
Parsons School of Design x UC Boulder<br>

**Platform:** Telegram

# Usage
**Telegram Bot -** @ElasticSpaceBot

## Install Required Packages

~~~
pip install -U aiogram paralleldots requests
~~~

## Obtaining credentials

* [**Telegram**](https://telegram.org) - Using your Telegram App, message @BotFather and create your bot.
Follow more instructions [here](https://core.telegram.org/bots#6-botfather)

* [**Parallel Dots**](https://www.paralleldots.com/emotion-analysis)

* [**imgFlip**](https://imgflip.com) - Signup on [imgFlip](https://imgflip.com/signup) and remeber your username and password :)


### Setting credentials in your local environment

~~~ python
# Run the following python commands
os.environ['telegram_bot_api_token'] = '<YOUR-TELEGRAM-BOT-TOKEN>'
os.environ['ParallelDots'] = '<YOUR-PARALLELDOTS-API-KEY>'
os.environ['imgflip_username'] = '<YOUR-IMGFLIP-USERNAME>'
os.environ['imgflip_password'] = '<YOUR-IMGFLIP-PASSWORD>'
~~~

### Running the script
~~~
python3 hackTheRemote.py
~~~

This should start your bot and display your bot name in terminal.

Let's begin the meme chat 😎🎉🎉

### APIs Used
* **Telegram Bot -** aiogram
* **Emotion Analysis -** ParallelDots
* **Meme Generator -** imgFlip

# Contributors
* [Akshay Baweja](https://akshaybaweja.com) - Parsons School of Design
* [Omar Hammad](https://github.com/hammadojh) - UC Boulder
