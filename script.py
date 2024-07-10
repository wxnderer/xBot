import tweepy, os, requests, io
from dotenv import load_dotenv
from PIL import Image
load_dotenv(override=True)
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

#Authenticate to X via v1 endpoint to upload media
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Retrieve random image from picsum
url = "https://picsum.photos/200/300"
response = requests.get(url)
image = Image.open(io.BytesIO(response.content))
image.save("image.jpg")
with open("image.jpg", "rb") as image:
    media_id = api.media_upload("image.jpg").media_id



#Authenticate to X via v2 endpoint to post
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)



client.create_tweet(text="Hi everyone!", media_ids=[media_id], user_auth=True)