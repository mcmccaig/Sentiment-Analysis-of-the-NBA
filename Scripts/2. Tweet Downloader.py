import GetOldTweets3 as got
import pandas as pd
import time
import datetime

#NBA team and city location dictionary
opponent_dict={'Atlanta Hawks': 'Atlanta',
               'Boston Celtics': 'Boston',
               'Brooklyn Nets': 'Brooklyn',
               'Charlotte Hornets': 'Charlotte',
               'Chicago Bulls': 'Chicago',
               'Cleveland Cavaliers': 'Cleveland',
               'Dallas Mavericks': 'Dallas',
               'Denver Nuggets': 'Denver',
               'Detroit Pistons': 'Detroit',
               'Golden State Warriors': 'San Francisco',
               'Houston Rockets': 'Houston',
               'Indiana Pacers': 'Indianapolis',
               'Los Angeles Clippers': 'Los Angeles',
               'Los Angeles Lakers': 'Los Angeles',
               'Memphis Grizzlies': 'Memphis',
               'Miami Heat': 'Miami',
               'Milwaukee Bucks': 'Milwaukee',
               'Minnesota Timberwolves': 'Minneapolis',
               'New Orleans Pelicans': 'New Orleans',
               'New York Knicks': 'New York',
               'Oklahoma City Thunder': 'Oklahoma City',
               'Orlando Magic': 'Orlando',
               'Philadelphia 76ers': 'Philadelphia',
               'Phoenix Suns': 'Phoenix',
               'Portland Trail Blazers': 'Portland',
               'Sacramento Kings': 'Sacramento',
               'San Antonio Spurs': 'San Antonio',
               'Toronto Raptors': 'Toronto',
               'Utah Jazz': 'Salt Lake City',
               'Washington Wizards': 'Washington D.C.'
}

def tweet_downloader(query, team):
    #loop to download the time and location specific tweets
    start_time = time.time()
    final_tweets = pd.DataFrame()
    for i in opponent_dict.values():
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(f'{query}')\
                                                   .setSince('2018-10-09')\
                                                   .setUntil('2019-04-11')\
                                                   .setWithin('30km')\
                                                   .setLang(Lang='en')\
                                                   .setNear(near=i)
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)
        end_time = time.time()
        print(f'Retrieving tweets from: {i}.             ', end='\r')
        for n in tweet:
            final_tweets = final_tweets.append({'ID': n.id,
                                                'Date': n.date,
                                                'User': n.username,
                                                'Tweet': n.text,
                                                'Game Location': i},
                                                ignore_index=True)

    final_tweets = final_tweets.sort_values(['Date']).reset_index(drop=True)

    final_tweets.to_csv(f'../data/tweets/{team}/raw/{query}_2018_2019_tweets.csv')

    end_time = time.time()
    print(f'Finished. Runtime: {end_time - start_time}           ')

#queries for each team
toronto = ['raptors',
           'kawhi',
           'kyle lowry',
           'pascal siakam']
houston = ['rockets',
           'james harden',
           'clint capela',
           'chris paul']
goldenstate = ['warriors',
            'kevin durant',
            'klay thompson',
            'steph curry']
newyork = ['knicks',
             'tim hardaway',
             'dennis smith',
             'emmanuel mudiay']
losangeles = ['lakers',
              'lebron',
              'kyle kuzma',
              'brandon ingram']

#download tweets
for i in toronto:
    tweet_downloader(i, 'raptors')

for i in houston:
    tweet_downloader(i, 'rockets')

for i in goldenstate:
    tweet_downloader(i, 'warriors')

for i in newyork:
    tweet_downloader(i, 'knicks')

for i in losangeles:
    tweet_downloader(i, 'lakers')
