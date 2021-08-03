from flask_restful import Resource

# request user to send

# {"subreddit": string, "topic": string}

# parse the data

# call the scraper

# return the scraped data to user


class RedditData(Resource):
  def get(self, ):

    return "Item not found for the id: {}".format(id), 404
