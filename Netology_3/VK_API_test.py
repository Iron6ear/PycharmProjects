#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from urllib.parse import urlencode, urlparse

AUS_URL = 'https://oauth.vk.com/authorize'
VER = '5.60'
APP_ID = '6042462'

auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'response_type': 'token',
    'scope': 'friends, status',
    'v': VER
}

print('?'.join((AUS_URL, urlencode(auth_data))))

token_url = 'https://oauth.vk.com/blank.html#access_token=8a6fe4e399187a4f02f4d06c6ba9e21f83c66218c42330842ebc2a3f9e0d8c3a3573823d92cbbece980dd&expires_in=86400&user_id=8845533'

o = urlparse(token_url)
fragment = dict((i.split('=') for i in o.fragment.split('&')))
access_token = fragment['access_token']

parameters = {'access_token': access_token, 'v': VER}

response = requests.get('https://api.vk.com/method/friends.getOnline', params=parameters)

for user_id in response.json()['response']:
    response = requests.get('https://api.vk.com/method/users.get', {'user_ids': user_id})
    print(response.json())
