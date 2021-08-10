import requests
import json


def get_reddit(subreddit, topic):
    """GET REQUEST to get the Json Data of Reddit Posts"""
    query = ""
    for char in topic:
        if char == " ":
            query += "%20"
        else:
            query += char
    request = None
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/search/.json?q={topic}&source=recent&restrict_sr=1'
        request = requests.get(base_url, headers={'User-agent': 'osu_project'})
    except requests.ConnectionError:
        print('Connection Error. Please try again later.')
    return request.json()


def reddit_scraper(subreddit, topic):
    data_all = get_reddit(subreddit, topic)
    data_posts = data_all['data']['children']
    n = 1
    all_posts = ""
    num_of_posts = len(data_posts) if len(data_posts) <= 10 else 10
    # combine all 10 posts in one text string
    for i in range(num_of_posts):
        data_curr = data_posts[i]
        all_posts += "# {}:".format(n) + data_curr['data']['title']
        all_posts += "\n"
        all_posts += data_curr['data']['selftext']
        n += 1

    # add each post separately
    sep_posts = {}
    for i in range(num_of_posts):
        data_curr = data_posts[i]
        post_key = "post {}".format(i+1)
        title = data_curr['data']['title']
        text = data_curr['data']['selftext']
        sep_posts[post_key] = {"title": title, "text": text}
        n += 1

    # combine both results together
    result = {"text": all_posts, "each post": sep_posts}
    return json.dumps(result)
