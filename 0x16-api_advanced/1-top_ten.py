#!/usr/bin/python3
""" module that contain top_ten function """


def top_ten(subreddit):
    """ function that queries the Reddit API and prints the titles of
        the first 10 hot posts listed for a given subreddit """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    r = requests.get(url)
    json_content = r.json()

    if (r.status_code == 200):
        count = 0
        for post in json_content['data']['children']:
            print(post['data']['title'])
            count += 1
            if count == 10:
                break
    else:
        return (None)
