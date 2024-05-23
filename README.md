# Python Telegram bot

Steps to Create a Telegram Bot and Get the Bot Token

1 - Create a Telegram Bot:

Open the Telegram app and search for "BotFather".<br>
Start a chat with BotFather and send the command /start.<br>
Create a new bot using the command /newbot.<br>
Follow the instructions to name your bot and get the bot token.<br>

2- Get the Chat ID of Your Channel:<br>

Add your bot to your Telegram channel.<br>
Send a message to the channel.<br>
Use the "https:// api.telegram.org/ bot<your_bot_token> /getUpdates" URL to get updates from your bot. You can find your channel’s chat ID in the JSON response.<br>

#Install Requests Library

pip install requests

