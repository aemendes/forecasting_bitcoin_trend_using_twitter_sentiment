import requests
import os
import json
import time
import math
import pandas as pd
import calendar
from random import seed
from random import randint

df = pd.DataFrame()
cal = calendar.Calendar()
seed(1)

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {
        'query': '(BTC OR Bitcoin OR #BTC OR #Bitcoin -RT) lang:en -is:retweet -is:reply -is:nullcast',
        'tweet.fields': 'created_at,in_reply_to_user_id',
        'max_results': '500',
        'start_time': '',
        'end_time': ''
    }

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

YEAR = 2021
MONTH = 4
HOURS_PER_DAY = 24
MAX_TWEETS_PER_DAY = 55000
ITERACTIONS_PER_HOUR = int(math.ceil(MAX_TWEETS_PER_DAY / HOURS_PER_DAY / 500))

# TODO: check month 5, days 4, 18, 30
# TODO: check month 7, days 18
# TODO: check month 4, days 1, 2, 3, 16, 26

def main():
    query_params['start_time'] = '{0}-{1}-01T00:00:00Z'.format(YEAR, MONTH)

    for day in cal.itermonthdays(YEAR, MONTH):
        if(day == 0 or day < 27): # Filter Out Days Don't needed
            continue

        if(day < 10):
            day = "0{}".format(day)

        for hour in range(HOURS_PER_DAY):
            # if(hour >= 23): # Filter Out Hours Don't needed
            #     continue

            if(hour < 10):
                hour = "0{}".format(hour)

            for i in range(ITERACTIONS_PER_HOUR):
                
                minutes = randint(0, 59)

                if(minutes < 10):
                    minutes = "0{}".format(minutes)

                query_params['end_time'] = "{0}-{1}-{2}T{3}:{4}:00.000Z".format(YEAR, MONTH, day, hour, minutes)

                json_response = connect_to_endpoint(search_url, query_params)
                #print(json.dumps(json_response, indent=4, sort_keys=True))

                filename = './data/year_{0}/month_{1}/day_{2}/{3}:{4}.json'.format(YEAR, MONTH, day, hour, minutes)

                os.makedirs(os.path.dirname(filename), exist_ok=True)

                with open(filename, 'w') as outfile:
                    json.dump(json_response, outfile)

                print("Retrieving data from {} to {}".format(query_params['start_time'], query_params['end_time']))
                time.sleep(2)

if __name__ == "__main__":
    main()