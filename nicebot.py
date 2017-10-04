import tweepy

CONSUMER_KEY = 'IWRWGlOjrjedAc8cy3mhPUHGa'
CONSUMER_SECRET = 'wNlfd9JTJfTow05Z0qidqI7TYbFxIOu9ZSI0yyypARfS3UieqG'
ACCESS_KEY = '915176419189313538-S9HdyZ0XQu7ZWFms5iqSAx3Vtot0xKL'
ACCESS_SECRET = 'Mj3dQwY6f7soYiXsztTbBAT9ow4GqvuOZp7ChNJbrTRt4'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(" Testing!!! ")
