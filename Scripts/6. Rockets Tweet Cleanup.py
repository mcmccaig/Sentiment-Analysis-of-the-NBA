import numpy as np
import pandas as pd
import glob

#create dataframe with all tweet query csvs in this folder concatenated
rockets = pd.concat([pd.read_csv(f, index_col=0) for f in glob.glob('../data/tweets/rockets/raw/*.csv')], ignore_index = True)
rockets['Date'] = pd.to_datetime(rockets['Date'])
CST = pd.Timedelta('6 hours')
rockets['Date'] = rockets['Date'] - CST
#remove links
rockets['Tweet'] = rockets['Tweet'].str.replace('http\S+|www.\S+', '', case=False)
#drop duplicate tweets
rockets = rockets.drop_duplicates('Tweet')
#reset index
rockets.reset_index(drop=True, inplace=True)
#export raw concatted csv
rockets.to_csv('../data/tweets/rockets/rockets_tweets_concat_raw.csv')

#remove query function
def remove_query(i):
    remove_index = rockets[rockets['Tweet'].str.contains(i, case=False)].index
    rockets.drop(remove_index, inplace = True)

# cleaning round 1
remove_query('spacex')
remove_query('rocket league')
remove_query('rocket test')
remove_query('rocket bar')
remove_query('rocket park')
remove_query('pets')
remove_query('DJGee')
remove_query('science')
remove_query('space')
remove_query('beer')
remove_query('rocket man')
remove_query('oil')
remove_query('LadyRocket')
remove_query('rocket fuel')
remove_query('screenwriting')
rockets.to_csv('../data/tweets/rockets/rockets_2018_tweets_v3_cleaned_v1.csv')

# Cleaning Round 2
remove_query('launcher')
remove_query('long ball')
remove_query('football')
remove_query('marvel')
remove_query('DCU')
remove_query('bakery')
remove_query('DJ Gee')
remove_query('rocket mortgage')
remove_query('little rocket')
remove_query('speed')
remove_query('music')
remove_query('team rocket')
remove_query('tattoo')
remove_query('moon rocket')
remove_query('flavors')
remove_query('rocket power')
remove_query('song')
remove_query('johnny')
remove_query('saturn')
remove_query('brew')
remove_query('raccoon')
remove_query('cat ')
remove_query('cats')
remove_query('exposure')
remove_query('bottle rocket')
rockets.to_csv('../data/tweets/rockets/rockets_2018_tweets_v3_cleaned_v2.csv')

# Cleaning Round 3
remove_query('riding')
remove_query('angel ')
remove_query('invest')
remove_query('nascar')
remove_query('montana')
remove_query('psycho')
remove_query('invest')
remove_query('russian')
remove_query('radio city')
remove_query('last rocket')
remove_query('takeoff')
remove_query('rocket ship')
remove_query('rocketship')
remove_query('stove')
remove_query('drones')
remove_query('aau')
remove_query('nasa')
remove_query('sky')
remove_query('jeans')
remove_query('mexican')
remove_query('buddha')
remove_query('steak')
remove_query('coffee')
remove_query('girl ')
remove_query('temptation')
remove_query('cheese')
remove_query('bomb')
remove_query('elon ')
remove_query('musk')
remove_query('fizz')
remove_query('israel')
remove_query('palestine')
remove_query('hamas')
remove_query('islam')
remove_query('sirens')
remove_query('heaven')
remove_query('copper')
remove_query('snot')
remove_query('crotch')
remove_query('bluejay')
remove_query('launch')
remove_query('border')
remove_query('thanos')
remove_query('nebula')
remove_query('avengers')
remove_query('groot')

#prep for export
rockets.sort_values('Date', inplace=True)
rockets = rockets.reset_index(drop=True)

#export
rockets.to_csv('../data/tweets/rockets/rockets_cleaned_tweets.csv')
