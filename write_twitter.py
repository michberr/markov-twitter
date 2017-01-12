import twitter
import os
from our_markov import open_and_read_file, update_chains, make_text
import sys
import pprint


def write_tweet(paths):

    chains = {}
    ngrams = 2

    for path in paths:
        # input_text = open_and_read_file(path)
        update_chains(path, chains, ngrams)

    # Produce random text
    random_text = make_text(chains)

    return random_text


def get_kanye():

    kanye_text = []

    statuses = api.GetUserTimeline(screen_name="kanyewest")
    for i in range(20):
        status_words = statuses[i].text.split()
        # Strip off links
        stripped_status = [word for word in status_words if "http" not in word]
        tweet_string = ' '.join(stripped_status)
        kanye_text.append(tweet_string)

    return kanye_text


api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                  consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                  access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                  access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

kanye_tweets = get_kanye()
text = write_tweet(kanye_tweets)
api.PostUpdate(text)




# Retweet and follow all tweets with #hackbrightgracejan17
grace_tweets = api.GetSearch(raw_query="q=%23hackbrightgracejan17")

for tweet in grace_tweets:
    try:
        api.PostRetweet(status_id=tweet.id)
    except twitter.error.TwitterError:
        pass

    try:
        api.CreateFriendship(screen_name=tweet.user.screen_name)
    except twitter.error.TwitterError:
        pass
