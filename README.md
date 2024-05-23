# Zip File Sender with Python to Telegram bot

Steps to Create a Telegram Bot and Get the Bot Token

Step 1- Create a Telegram Bot:

Open the Telegram app and search for "BotFather".<br>
Start a chat with BotFather and send the command /start.<br>
Create a new bot using the command /newbot.<br>
Follow the instructions to name your bot and get the bot token.<br>

Step 2- Get the Chat ID of Your Channel:<br>

Add your bot to your Telegram channel.<br>
Send a message to the channel.<br>
Use the "https:// api.telegram.org/ bot<your_bot_token> /getUpdates" URL to get updates from your bot. You can find your channel’s chat ID in the JSON response.<br>

#Install Requests Library

pip install requests


Step 3: Send a Message to the Channel
Send a message to the channel. This will ensure that there is a recent activity for the bot to fetch.

Step 4: Get Updates Using Bot API
You can use the getUpdates method to fetch the latest messages and activities involving your bot. Here's how you can do it:

Open your browser and enter the following URL:


Copy code

https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates

Replace <YOUR_BOT_TOKEN> with your actual bot token.

Step 5: Look for the chat ID:

The JSON response will contain information about the updates, including messages sent to the channel.
Find the "chat" object within the "message" object. The "id" field inside the "chat" object is your channel ID. Note that it usually starts with -100.


