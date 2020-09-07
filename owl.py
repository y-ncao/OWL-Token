#!/usr/bin/env python

import requests
import time
from datetime import datetime


AUTHORITY = 'wzavfvwgfk.execute-api.us-east-2.amazonaws.com'
ORIGIN = 'https://overwatchleague.com'
API_URL = "https://api.overwatchleague.com/live-match"
LOGIN_URL = "https://api.overwatchleague.com/login"
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
AC = 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'


def get_owl_live_match():
    response = requests.get(API_URL)
    js_res = response.json()
    match = js_res['data']['liveMatch']
    if not match:
        return ('', '')

    match_id = match['id']
    match_status = js_res['data']['liveMatch']['liveStatus']
    referer = 'https://overwatchleague.com/en-us/match/{0}/'.format(match_id)
    return (match_status, referer)

post_headers = {
    'authority': AUTHORITY,
    'accept': 'application/json',
    'x-origin': 'overwatchleague.com',
    'user-agent': UA,
    'content-type': 'application/json',
    'origin': ORIGIN,
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': AC,
}

option_headers = {
    'authority': AUTHORITY,
    'accept': '*/*',
    'access-control-request-method': 'POST',
    'access-control-request-headers': 'content-type,x-origin',
    'origin': ORIGIN,
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-dest': 'empty',
    'user-agent': UA,
    'accept-language': AC,
}

# == Replace the accountId below with your appuid ==
data = '{"accountId":"12345678","type":"video_player","entryId":"bltfed4276975b6d58a"}'
url = 'https://wzavfvwgfk.execute-api.us-east-2.amazonaws.com/production/v2/sentinel-tracking/owl'

if __name__ == "__main__":
    count = 0
    while True:
        now = datetime.now()
        try:
            match_status, referer = get_owl_live_match()
            if match_status in ['', 'UPCOMING']:
                print('-'*10, 'View Time: {0}min. Now: {1}'.format(count, now.strftime("%H:%M:%S")), '-'*10)
                print('Match Not Started Yet')
                time.sleep(60)
                continue
            post_headers['referer'] = referer
            option_headers['referer'] = referer

            post_response = requests.post(url, headers=post_headers, data=data)
            option_response = requests.options(url, headers=option_headers)
            print('-'*10, 'View Time: {0}min. Now: {1}'.format(count, now.strftime("%H:%M:%S")), '-'*10)
            print("Post Response JSON: ", post_response.json())
            print("Option Response Code: ", option_response.status_code)
        except Exception as e:
            print('Failed request')
            print(e)
            time.sleep(120)


        count += 1
        time.sleep(60)
