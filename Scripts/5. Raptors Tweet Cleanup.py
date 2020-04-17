import numpy as np
import pandas as pd
import glob

#create dataframe with all csvs in this folder concatenated
raptors = pd.concat([pd.read_csv(f, index_col=0) for f in glob.glob('../data/tweets/raptors/raw/*.csv')], ignore_index = True)
#datetime conversion
raptors['Date'] = pd.to_datetime(raptors['Date'])
EST = pd.Timedelta('5 hours')
raptors['Date'] = raptors['Date'] - EST
#remove hyperlinks
raptors['Tweet'] = raptors['Tweet'].str.replace('\w+:\/\/\S+', '', case=False)
#drop duplicate tweets
raptors = raptors.drop_duplicates('Tweet')
#reset index
raptors.reset_index(drop=True, inplace=True)
#export raw concatted csv
raptors.to_csv('../data/tweets/raptors/raptors_tweets_concat_raw.csv')

def remove_query(i):
    remove_index = raptors[raptors['Tweet'].str.contains(i, case=False)].index
    raptors.drop(remove_index, inplace = True)

#cleaning
remove_query('ford')
remove_query('racing')
remove_query('universal')
remove_query('jurassic')
remove_query('soccer')
remove_query('Lazer Raptor')
remove_query('Laser Raptor')
remove_query('encounter')
remove_query('adventures')
remove_query('exposure')
remove_query('halloween')
remove_query('little raptors')
remove_query('vertimax')
remove_query('bird')
remove_query('falcon')
remove_query('owl ')
remove_query('zoo')
remove_query('museum')
remove_query('aurora')
remove_query('rutgers')
remove_query('space raptor')
remove_query('paint')

#prep for export
raptors.sort_values('Date', inplace=True)
raptors = raptors.reset_index(drop=True)
#export
raptors.to_csv('../data/tweets/raptors/raptors_cleaned_tweets.csv')
