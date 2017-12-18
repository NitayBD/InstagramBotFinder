from InstagramAPI import InstagramAPI
import json
from connector import *



def find_id_by_name(username):
    print instagram.searchUsers(username)
    # print json.dumps(instagram.LastJson, sort_keys=True, indent=4)
    private_key = instagram.LastJson['users'][0]['pk']
    print private_key
    return private_key


def get_hashtags_from_posts_by_id(username_id):
    instagram.getUserFeed(find_id_by_name(username_id))
    print json.dumps(instagram.LastJson, sort_keys=True, indent=4)
    media_dict = {}
    for item in instagram.LastJson['items']:
        media_dict[item['pk']] = item['text'][item['text'].find('#'):].replace(' ', '').split('#')


def get_following_number(username_id):
    instagram.getUsernameInfo(username_id)
    return instagram.LastJson['user']['following_count']


def get_followers_number(username_id):
    instagram.getUsernameInfo(username_id)
    print json.dumps(instagram.LastJson, sort_keys=True, indent=4)
    return instagram.LastJson['user']['follower_count']



# datetime.datetime.fromtimesta
# mp(
#     int("1284101485")
# ).strftime('%Y-%m-%d %H:%M:%S')





