# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

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

search = input("Enter a term to search for: ")
public_tweets = api.search(search)


total_subjectivity = 0;
total_polarity = 0;
total_ct = 0;

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	total_polarity += analysis.sentiment.polarity
	total_subjectivity += analysis.sentiment.subjectivity
	total_ct += 1;

print("Average subjectivity is", total_subjectivity / total_ct)
print("Average polarity is", total_polarity / total_ct)
