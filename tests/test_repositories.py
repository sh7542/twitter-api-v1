from unittest import TestCase
from app.repository import TweetRepository
from app.models import Tweet

class TestTweetRepository(TestCase):

#    def test_new_repo(self):
#        tweetrepo = TweetRepository()
#        self.assertEqual(len(tweetrepo.tweets), 0)

#    def test_add_tweet(self):
#        tweetrepo = TweetRepository()
#        tweet = Tweet("First test tweet")
#        tweetrepo.add(tweet)
#        self.assertEqual(tweetrepo.tweets[0].id, 1)

#    def test_get_tweet(self):
#        tweetrepo = TweetRepository()
#        tweet = Tweet("First test tweet")
#        tweetrepo.add(tweet)
#        tweet = Tweet("Second test tweet")
#        tweetrepo.add(tweet)
#        res = tweetrepo.get(2)
#        self.assertEqual(res.text, "Second test tweet")

    def test_instance_variables(self):
        repository = TweetRepository()
        self.assertEqual(len(repository.tweets), 0)

    def test_add_tweet(self):
        repository = TweetRepository()
        tweet = Tweet("a new tweet")
        repository.add(tweet)
        self.assertEqual(len(repository.tweets), 1)

    def test_auto_increment_of_ids(self):
        repository = TweetRepository()
        first_tweet = Tweet("a first tweet")
        repository.add(first_tweet)
        self.assertEqual(first_tweet.id, 1)
        second_tweet = Tweet("a second tweet")
        repository.add(second_tweet)
        self.assertEqual(second_tweet.id, 2)

    def test_get_tweet(self):
        repository = TweetRepository()
        tweet = Tweet("a new tweet")
        repository.add(tweet)
        self.assertEqual(tweet, repository.get(1))
        self.assertIsNone(repository.get(2))







