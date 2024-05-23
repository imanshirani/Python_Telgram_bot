# Python_Telgram_bot

Steps to Create a Telegram Bot and Get the Bot Token
Create a Telegram Bot:

Open the Telegram app and search for "BotFather".
Start a chat with BotFather and send the command /start.
Create a new bot using the command /newbot.
Follow the instructions to name your bot and get the bot token.
Get the Chat ID of Your Channel:

Add your bot to your Telegram channel.
Send a message to the channel.
Use the https://api.telegram.org/bot<your_bot_token>/getUpdates URL to get updates from your bot. You can find your channel’s chat ID in the JSON response.
