import json
import requests
import tweepy
import openai
import time
from tweepy.streaming import StreamingClient

Consumer_Key = "YOUR CONSUMER KEY"
Consumer_Secret = "YOUR CONSUMER SECRET"
Access_Token = "YOUR ACCESS TOKEN"
Access_Secret = "YOUR ACCESS SECRET"
Bearer_Token = "YOUR BEARER TOKEN"
Client_ID = "YOUR CLIENT ID"
Client_Secret = "YOUR CLIENT SECRET"
#TAKE THAT INF FROM YOUR APP 
user_id = "YOUR TWITTER ACC USER ID"

def generate_roast():
    openai.api_key = 'YOUR API KEY IN OPEN AI'
    openai.organization = 'ORGANIZATION IN OPEN AI'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="generate a funny short text",
        temperature=0.7,
        max_tokens=2000,
    )
    roast_text = response.choices[0].text.strip()
    return roast_text


client = tweepy.Client(
    bearer_token=Bearer_Token,
    consumer_key=Consumer_Key,
    consumer_secret=Consumer_Secret,
    access_token=Access_Token,
    access_token_secret=Access_Secret
)

tweetfields = ['referenced_tweets,author_id']
replied_mentions = set()  # Track the mentions that have been replied to

while True:
    mentions = client.get_users_mentions(id=user_id, tweet_fields=tweetfields)
    
    for mention in mentions.data:
        mention_id = mention["id"]
        if mention_id not in replied_mentions:
            users_id = mention["author_id"]
            user = client.get_user(id=users_id)
            User_Name = user.data["username"]
            print(User_Name)
            print(mention_id)            
            response = client.create_tweet(in_reply_to_tweet_id=mention_id, text=generate_roast())
            print(response)
            replied_mentions.add(mention_id)
    
    time.sleep(60)  # Wait for 60 seconds before checking for new mentions again
