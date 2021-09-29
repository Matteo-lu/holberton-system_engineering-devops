#!/usr/bin/python3
""" module that contain number_of_subscribers function """


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns
        the number of subscribers"""
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    r = requests.get(url)
    json_content = r.json()

    if (r.status_code == 200):
        return(json_content['data']['subscribers'])
    else:
        return (0)
