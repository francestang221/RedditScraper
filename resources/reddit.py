from flask import request
from flask_restful import Resource
import RedditScraper
import json


class Reddit(Resource):
    def post(self):
        user_request = json.loads(request.data)
        print(user_request)
        subreddit = user_request['subreddit']
        topic = user_request['topic']
        return json.loads(RedditScraper.reddit_scraper(subreddit, topic))

        #  WIP: error handling
        # check if subreddit exists
        # status code check
