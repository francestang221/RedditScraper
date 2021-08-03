from flask import Flask, jsonify, request
from flask_restful import Api
import json

import RedditScraper
from resources.reddit import Reddit

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)

api = Api(app)

api.add_resource(Reddit, "/reddit")


@app.route("/reddit", methods=["GET", "POST"])
def reddit_data():
    user_request = json.loads(request.data)
    subreddit = user_request['subreddit']
    topic = user_request['topic']
    data = RedditScraper.reddit_scraper(subreddit, topic)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
