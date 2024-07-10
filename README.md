# xBot 🤖

xBot is a simple Python script that retrieves a random image from Picsum and posts it to X (formerly known as Twitter) using the Tweepy library. This script works using X's free tier API.

We use both v1 and v2 APIs in this project for the following reasons:

- **v1 API**: The v1 API is used for media upload functionality. This is because the media upload endpoint is not yet available in the v2 API.
- **v2 API**: The v2 API is used for posting tweets as you can't post tweets on free tier through v1 API.

## Prerequisites 📋

Before you begin, ensure you have met the following requirements:

- You have Python 3.x installed on your machine.
- You have a Twitter/X Developer account and have created an app to obtain the necessary API keys and tokens (_YOU NEED TO USE OAuth1 credentials!!_).
- Read/Write permissions within your X app settings.

## Installation 🛠️

1. Clone the repository or download the script.
2. Navigate to the project directory.
3. Install the required Python packages using pip:

pip install -r requirements.txt

## Setup ⚙️

Create a `.env` file in the project directory and add your Twitter/X API credentials:

CONSUMER_KEY=your_consumer_key
CONSUMER_KEY_SECRET=your_consumer_key_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret

Ensure the `.env` file is in the same directory as `script.py`.

## Usage 🚀

To run the script, execute the following command:

python script.py

The script will:

1. Authenticate to X using the provided API credentials.
2. Retrieve a random image from Picsum and save it to the working directory.
3. Upload the image to X via v1 API.
4. Post a tweet with the uploaded image via v2 API.

## License 📄

This project is licensed under the MIT License. See the LICENSE file for details.
