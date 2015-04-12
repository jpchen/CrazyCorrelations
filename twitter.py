from twython import Twython

APP_KEY = 'oaQ4UtmRG5hB7yh1R05HoAQCu'
APP_SECRET = 'bOUVsRnDexctkMl05lo4felxvuU2LhhJt3g4xLz3FbM8wpm7GO'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
friends = twitter.get_friends_ids(screen_name = "NPhardon")

for follower_id in friends['ids']:
	params = {'user_id':follower_id, 'count':200 }
	print twitter.get_user_timeline(**params)
