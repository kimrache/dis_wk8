# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

import tweepy
import nltk

# Unique code from Twitter
access_token = "796822723083325440-CObpW1SgnHGahZofbWPehr477q4zLnD"
access_token_secret = "EQuKPjhoV8pf79n8sWEJ1QSkFouQWQBkt9vfcbwIkzZfn"
consumer_key = "ghPC3Y6S9EcfTcPLKy9l9fptD"
consumer_secret = "3bMOGDoQDrqDHzYW0ycO3O7YypOFIkmCkpHIVreqJCtPpaXZtl"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

filename = "corgi.jpg"

api.update_with_media(filename, status="#UMSI-206 #Proj3")