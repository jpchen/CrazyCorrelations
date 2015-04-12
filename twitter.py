from twython import Twython
import indicoio
from indicoio import text_tags, batch_text_tags


#this shit is private yo
APP_KEY = 'oaQ4UtmRG5hB7yh1R05HoAQCu'
APP_SECRET = 'bOUVsRnDexctkMl05lo4felxvuU2LhhJt3g4xLz3FbM8wpm7GO'
indicoio.config.api_key = "254f8cd9f1827ee630222fde1a9b3fd0"

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
friends = twitter.get_friends_ids(screen_name = "NPhardon")

with open('out', 'w') as f:
	for follower_id in friends['ids']:
		params = {'user_id':follower_id, 'count':10 }
		tweets = twitter.get_user_timeline(**params)
		for tweet in tweets:
			encoded = tweet['text'].encode("utf8")
			print text_tags(encoded)
			#f.write(str(text_tags(encoded)))

