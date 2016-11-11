# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# Unique code from Twitter
access_token = "796822723083325440-CObpW1SgnHGahZofbWPehr477q4zLnD"
access_token_secret = "EQuKPjhoV8pf79n8sWEJ1QSkFouQWQBkt9vfcbwIkzZfn"
consumer_key = "ghPC3Y6S9EcfTcPLKy9l9fptD"
consumer_secret = "3bMOGDoQDrqDHzYW0ycO3O7YypOFIkmCkpHIVreqJCtPpaXZtl"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
api = tweepy.API(auth)

# image file
filename = "corgi.jpg"

# posting tweet with image and hashtags
api.update_with_media(filename, status="#UMSI-206 #Proj3")