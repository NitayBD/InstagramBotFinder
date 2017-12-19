__author__ = 'Administrator'
from Data_Extraction import *
import random
import math


def if_bot_by_hustags(username_id):
    count12 = 0
    count23 = 0

    hashtag_list = get_hashtags_from_posts_by_id(username_id)
    hushtags1 = hashtag_list[random.choice(hashtag_list.keys())]
    hushtags2 = hashtag_list[random.choice(hashtag_list.keys())]
    hushtags3 = hashtag_list[random.choice(hashtag_list.keys())]
    count12 = compare_lists(hushtags1, hushtags2)
    count23 = compare_lists(hushtags2, hushtags3)
    if math.fabs(count12 - count23) < 10:
        return True
    return False


def compare_lists(list1, list2):
    counter = 0
    for idx, item1 in enumerate(list1):
        for item2 in list2[idx:]:
            if item1 == item2:
                counter += 1

    return counter


def dif_folowers_folowing(folowers, folowing):
    if folowing / float(folowers) < 0.23:
        return True
    return False


def photo_dates(photosdates):
    count = 0
    backphotodate = photosdates
    for index, photosdate1 in enumerate(photosdates):
        for dates in photosdates[index:]:
             if photosdate1.value() == dates:
                 count += 1
        if count > 3:
             return True
    return False


def Is_Bot(username):
    username_id = find_id_by_name(username)
    if if_bot_by_hustags(get_hashtags_from_posts_by_id(username_id)) and dif_folowers_folowing(get_followers_number(username_id), get_following_number(username_id)) == True:
        return "hell of a bot"
    elif if_bot_by_hustags(get_hashtags_from_posts_by_id()) and photo_dates(Photodates) == True:
        return "hell of a bot"
    # elif dif_folowers_folowing(getfolowers, getfolowing) and photo_dates(Photodates) == True:
    #     return "hell of a bot"
    return "not even close"


print Is_Bot('ruicampos_fotografia')