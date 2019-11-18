import tweepy
from credentials import CONSUMER_SECRET,CONSUMER_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET
from time import sleep

content = {
	"elonmusk":[
		"Hey what's the protocol if a self driving car is involved in an accident. Who takes the liability?",
		"Do you think space debris will hinder the mars project in any way?",
		"What do you think is better, A space elevator or a space tether?"
	],
	"speigel_spike":["Sample tweet"]
}

def follow():
	for screen_name in content:
		timeline = api.user_timeline(screen_name)
		for tweet in timeline:
			latest_tweet_id[screen_name] = tweet.id
			break

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

latest_tweet_id = dict()
follow()

while(True):
	for screen_name in content:
		timeline = api.user_timeline(screen_name)
		for tweet in timeline:
			if((tweet.id != latest_tweet_id[screen_name]) & (len(content[screen_name]) != 0)):
				api.update_status('@' + screen_name + ' ' + content[screen_name][0], tweet.id)
				latest_tweet_id[screen_name] = tweet.id
				content[screen_name].pop(0)
			break
	sleep(5)






