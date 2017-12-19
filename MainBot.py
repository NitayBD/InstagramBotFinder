from neo4j.v1 import GraphDatabase
from Data_Extraction import *
import random, sys
from threading import Thread
from Queue import Queue

concurrent = 200

user_dict = {}
counter = 0
q = Queue(concurrent * 2)


def do_work():
    while True:
        username_id = q.get()
        following = get_following(username_id)
        do_something_with_result(username_id, following)
        q.task_done()


def do_something_with_result(username_id, following):
    global user_dict, counter, q
    user_dict[username_id] = [x['pk'] for x in following]
    if counter < 10 and following:
        next_list = choose_ten_random(following)
        for new_good_item in next_list:
            q.put(new_good_item['pk'])
        counter += 1


def choose_ten_random(old_list):
    new_list = []
    for x in range(10):
        new_list.append(random.choice(old_list))

    return new_list


first_account = 'ruicampos_fotografia'
username_id = find_id_by_name(first_account)
following = get_following(username_id)
ten_list = choose_ten_random(following)


for i in range(concurrent):
    t = Thread(target=do_work)
    t.daemon = True
    t.start()
try:
    for item in ten_list:
        q.put(item['pk'])
    q.join()
except KeyboardInterrupt:
    sys.exit(1)


print user_dict
shakes = 0
crosses = 0
for key, val in user_dict.iteritems()[0]:
    if key in get_following(val):
        shakes += 1













