from neo4j.v1 import GraphDatabase
from Data_Extraction import *
import random, sys
from threading import Thread
from Queue import Queue
import requests

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
    if counter < 1 and following:
        next_list = choose_ten_random(following)
        for new_good_item in next_list:
            q.put(new_good_item['pk'])
        counter += 1


def choose_ten_random(old_list):
    new_list = []
    for x in range(10):
        new_list.append(random.choice(old_list))

    return new_list


first_account = 'krown_loyal_inspirations'
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
# shakes = 0
# crosses = 0
# for key, val in user_dict.iteritems()[0]:
#     if key in get_following(val):
#         shakes += 1

headers = {'Content-type': 'application/json', 'Accept': 'application/json; charset=UTF-8'}
your_data = {'statements': []}
for key in user_dict.keys():
    your_data['statements'].append({'statement': 'CREATE (user%d:User {name: "%d"})' % (key, key)})
r = requests.post('http://localhost:7474/db/data/transaction/commit', json=your_data, headers=headers)
print your_data['statements']
print r.json
your_data['statements'] = []


for values in user_dict.values():
    for value in values:
        your_data['statements'].append({'statement': 'CREATE (user%d:User {name: "%d"})' % (value, value)})
    r = requests.post('http://localhost:7474/db/data/transaction/commit', json=your_data, headers=headers)
    print your_data['statements']
    print r.json
    your_data['statements'] = []


know_string = ''
for key, values in user_dict.iteritems():
    for value in values:
        know_string += '(user%d)-[:KNOWS]->(user%d),' % (key, value)
    your_data['statements'] = [{'statement': 'CREATE ' + know_string[:-1]}]
    r = requests.post('http://localhost:7474/db/data/transaction/commit', json=your_data, headers=headers)
    print your_data['statements']
    print r.json
    your_data['statements'] = []














