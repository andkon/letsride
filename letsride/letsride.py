from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API


CONSUMER_KEY = 'yNNHTkCgdMrhzJAWS1GqBw'
CONSUMER_SECRET = 'Tq7K8h3OyOtXxPeisSwKoJwK8O6Q2QkCaf8BMtEW4'
ACCESS_KEY = '2347331544-bSLI7Ozf8mPIKHd9vkG6pfMedUjuAb9SD8SxeJ1'
ACCESS_SECRET = 'aMAbds01ZkghQ6ZKZJqhzGawPhWyiikdvcpsxmmbdJnRU'

class StdOutListener(StreamListener):
	"""
	This receives and handles tweets from the stream.
	"""
	def on_status(self, status):
		if status.in_reply_to_screen_name == "WillYouRide":
			gamer_screen_name = status.author.screen_name
			received_status_id = status.id
			previous_status_id = status.in_reply_to_status_id
			import pdb; pdb.set_trace()
			received_status_text = status.text
			# Here, the gamer hasn't replied to one of our previous tweets:
			if previous_status_id is None:
				if not "bike" in received_status_text:
					# Get the gamer back to where they should be.
					status = "@"+gamer_screen_name+" to get riding, tweet the word 'bike' at me. To pick up where you left off, @-reply from my latest tweet."
					api.update_status(status, received_status_id)
					print 'The gamer didnt reply to a tweet'
				else:
					# The game starts
					import pdb; pdb.set_trace()
					status = "@"+gamer_screen_name+" You're riding a bike. It's after midnight, and it still feels like 30 above. Sticky air, thunder on the way."
					api.update_status(status, received_status_id)
		
			else:
				# here's where you run the game logic
				print "@%s replied to this tweet %s with this text: %s" % (gamer_screen_name, previous_status_id, received_status_text)
				# Basically, 

	def on_error(self, status_code):
		print status_code
		return False

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = API(auth)

    stream = Stream(auth, l)
    stream.userstream()