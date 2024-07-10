import tweepy, os, requests, io
from dotenv import load_dotenv
from PIL import Image

def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
    #v1 Auth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #v2 Auth
    client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
    return api,client

def post_tweet(auth,text_content,media_url):
    api = auth[0]
    client = auth[1]
    response = requests.get(media_url)
    image = Image.open(io.BytesIO(response.content))
    image.save("image.jpg")
    with open("image.jpg", "rb") as image:
        media_id = api.media_upload("image.jpg").media_id

    return client.create_tweet(text=text_content, media_ids=[media_id], user_auth=True)

#Example

load_dotenv(override=True)

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth_sample = authenticate(consumer_key, consumer_secret, access_token, access_token_secret)

media_url_sample = "https://picsum.photos/200/300"
text_content_sample = "Hello  ̶T̶w̶i̶t̶t̶e̶r̶ X ! This is a useless tweet with a useless image ! 😊"

post_tweet(auth_sample,text_content_sample,media_url_sample)

