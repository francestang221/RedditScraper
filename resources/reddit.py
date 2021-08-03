import requests
from flask_restful import Resource
import RedditScraper

user_request = {'subreddit': 'OSUOnlineCS', 'topic': 'CS 225'}


class Reddit(Resource):
    def post(self):
        subreddit = user_request['subreddit']
        topic = user_request['topic']
        if subreddit and topic:
            return RedditScraper.reddit_scraper(subreddit, topic)
        return 'error'
