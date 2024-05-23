import requests

# Replace with your bot token and channel chat ID
bot_token = 'YOUR_BOT_TOKEN'
channel_id = 'your_channel_id'

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, data=payload)
    return response.json()

def send_file(token, chat_id, file_path):
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    files = {
        'document': open(file_path, 'rb')
    }
    payload = {
        'chat_id': chat_id
    }
    response = requests.post(url, data=payload, files=files)
    return response.json()

if __name__ == "__main__":
    message = "Here is the information you requested and the zip file."
    zip_file_path = 'path/to/your/file.zip'
    
    # Send message
    message_response = send_message(bot_token, channel_id, message)
    print("Message response:", message_response)
    
    # Send zip file
    file_response = send_file(bot_token, channel_id, zip_file_path)
    print("File response:", file_response)
