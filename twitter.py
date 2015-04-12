from twython import Twython
import indicoio
from indicoio import text_tags, batch_text_tags
import random, sys
from collections import Counter

#this shit is private yo
APP_KEY = 'oaQ4UtmRG5hB7yh1R05HoAQCu'
APP_SECRET = 'bOUVsRnDexctkMl05lo4felxvuU2LhhJt3g4xLz3FbM8wpm7GO'
indicoio.config.api_key = "254f8cd9f1827ee630222fde1a9b3fd0"
news = ['Obama and Castro Meeting for the first time in half a century',
        'Hillary Clinton\'s Calculus on Embracing Obama',
        'Red Sox Trumps Yankees in 19-Inning Game',
        'Empty Ebolo Clinics in Liberia hurting US Relief Effort',
        'California Instating first Water Restrictions and Regulations']

def scrape(arg):
	results = {}
	twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
	ACCESS_TOKEN = twitter.obtain_access_token()

	twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
	friends = twitter.get_friends_ids(screen_name = arg)

	with open('out', 'w') as f:
		for follower_id in friends['ids']:
			params = {'user_id':follower_id, 'count':3 }
			tweets = twitter.get_user_timeline(**params)
			for tweet in tweets:
				encoded = tweet['text'].encode("utf8")
				results = dict(Counter(results) + Counter(text_tags(encoded)))
				#random.choice(news)
				#f.write(str(text_tags(encoded)))
		print results

if __name__ == "__main__":
    scrape(sys.argv[1:])