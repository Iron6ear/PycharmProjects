#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from urllib.parse import urlencode, urlparse
import networkx
import matplotlib.pyplot as plt

AUS_URL = 'https://oauth.vk.com/authorize'
VER = '5.60'
APP_ID = '6042462'
BASE_USER_ID = 8845533
result_graph = networkx.Graph()
result_graph.add_node(BASE_USER_ID)

auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'response_type': 'token',
    'scope': 'friends, status',
    'v': VER
}

print('?'.join((AUS_URL, urlencode(auth_data))))

token_url = 'https://oauth.vk.com/blank.html#access_token=02824a01b7bb67fea2050d4aee3e034329925f86428428a840a56bd4684c4bccb27c85190a2f1609bde43&expires_in=86400&user_id=8845533'

o = urlparse(token_url)
fragment = dict((i.split('=') for i in o.fragment.split('&')))
access_token = fragment['access_token']

parameters = {
    'access_token': access_token,
}

response = requests.get('https://api.vk.com/method/friends.get', params=parameters)

# for user_id in response.json()['response']:
#     response = requests.get('https://api.vk.com/method/users.get', {'user_ids': user_id})
#     print(response.json())

all_friends = response.json()['response']
result_graph.add_nodes_from(all_friends)
for edges in all_friends:
    result_graph.add_edge(BASE_USER_ID, edges)

for user_id in response.json()['response']:
    try:
        friends_of_friend = requests.get('https://api.vk.com/method/friends.get', params={'user_id': user_id})
        result_graph.add_nodes_from(friends_of_friend.json()['response'])
        for edges in friends_of_friend.json()['response']:
            result_graph.add_edge(user_id, edges)
    except KeyError:
        pass

networkx.draw(result_graph)
plt.show()
