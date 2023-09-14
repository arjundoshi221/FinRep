import tweepy

# Set your API keys and access tokens
consumer_key = "x5qz2lK3M038KEPExiKRu7YG2"
consumer_secret = "mJfFYzWAMCyJS980FjunnXParVEIbSvyKNmZLEnnfxqGOhP8yb"
access_token = "1281913118415712257-jxMZ4L5pJJkDdsR6e2rKMZf2wT34ou"
access_token_secret = "X6ltAd1tdiWoumllAujSuMS87FYFXVcKjeXbJzpftXFxg"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# # Create a Tweepy API object
# api = tweepy.API(auth, wait_on_rate_limit=True)

# # Define the search query and the number of tweets to retrieve
# search_query = "ishandandekar"
# num_tweets = 5  # You can adjust this number as needed

# # Retrieve tweets
# tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang="en").items(num_tweets)

# # Process and print the tweets
# for tweet in tweets:
#     print(tweet.text)

public_tweets = api.home_timeline()
print(public_tweets[0])
