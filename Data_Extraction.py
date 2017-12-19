from InstagramAPI import InstagramAPI
import json
import datetime
from connector import *


def find_id_by_name(username):
    print instagram.searchUsers(username)
    print json.dumps(instagram.LastJson, sort_keys=True, indent=4)
    private_key = None
    try:
        private_key = instagram.LastJson['users'][0]['pk']
    except:
        pass
    print private_key
    return private_key


def get_hashtags_from_posts_by_id(username_id):
    try:
        instagram.getUserFeed(username_id)
    except:
        pass
    print '||||||||||||||||'
    print json.dumps(instagram.LastJson, sort_keys=True, indent=4)
    print '||||||||||||||||'
    media_dict = {}
    for item in instagram.LastJson['items']:
        media_dict[item['pk']] = item['caption']['text'][item['caption']['text'].find('#'):].replace(' ', '').split('#')

    return media_dict


def get_following_number(username_id):
    instagram.getUsernameInfo(username_id)
    return instagram.LastJson['user']['following_count']


def get_followers_number(username_id):
    instagram.getUsernameInfo(username_id)
    print json.dumps(instagram.LastJson, sort_keys=True, indent=4)
    return instagram.LastJson['user']['follower_count']


def get_posts_dates(username_id):
    instagram.getUserFeed(username_id)
    print '||||||||||||||||'
    print json.dumps(instagram.LastJson, sort_keys=True, indent=4)
    print '||||||||||||||||'
    dates_dict = {}
    for item in instagram.LastJson['items']:
        dates_dict[item['pk']] = datetime.datetime.fromtimestamp(int(item['caption']['created_at'])).strftime('%Y-%m-%d')

    return dates_dict



username_id = find_id_by_name('ruicampos_fotografia')
print get_posts_dates(username_id)

# print get_hashtags_from_posts_by_id(find_id_by_name('ruicampos_fotografia'))

# datetime.datetime.fromtimesta
# mp(
#     int("1284101485")
# ).strftime('%Y-%m-%d %H:%M:%S')





