__author__ = 'Administrator'
import Data_Extraction
import random
import math


def if_bot_by_hustags(hustagsid):
    counth12 = 0
    counth23 = 0
    hustags1 = random.choice(hustagsid[hustags])
    hustags2 = random.choice(hustagsid[hustags])
    hustags3 = random.choice(hustagsid[hustags])
    for hushtag1 in hushtags1:
        for hushtag2 in hushtag2:
            if hushtag1 == hushtag2:
                count12 += 1
    for hushtag2 in hushtags2:
        for hushtag3 in hushtag3:
            if hushtag2 == hushtag3:
                count23 += 1
    if math.abs(counth12 - counth23) < 10:
        return True
    return False


def dif_folowers_folowing(folowers, folowing):
    if folowing / folowers < 0.23:
        return True
    return false


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


def Is_Bot():
    if if_bot_by_hustags(Data_Extraction.get_hashtags) and dif_folowers_folowing(Data_Extraction.getfolowers, Data_Extraction.getfolowing) == True:
        return "hell of a bot"
    elif if_bot_by_hustags(Data_Extraction.get_hashtags) and photo_dates(Data_Extraction.Photodates) == True:
        return "hell of a bot"
    elif dif_folowers_folowing(Data_Extraction.getfolowers, Data_Extraction.getfolowing) and photo_dates(Data_Extraction.Photodates) == True:
        return "hell of a bot"
    return "not even close"
