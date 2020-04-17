import numpy as np
import pandas as pd
import glob

#create dataframe with all csvs in this folder concatenated
lakers = pd.concat([pd.read_csv(f, index_col=0) for f in glob.glob('../data/tweets/lakers/raw/*.csv')], ignore_index = True)
#datetime conversion
lakers['Date'] = pd.to_datetime(lakers['Date'])
PST = pd.Timedelta('8 hours')
lakers['Date'] = lakers['Date'] - PST
#remove hyperlinks
lakers['Tweet'] = lakers['Tweet'].str.replace('\w+:\/\/\S+', '', case=False)
#drop duplicate tweets
lakers = lakers.drop_duplicates('Tweet')
#reset index
lakers.reset_index(drop=True, inplace=True)
#export raw concatted csv
lakers.to_csv('../data/tweets/lakers/lakers_tweets_concat_raw.csv')

#remove query function
def remove_query(i):
    remove_index = lakers[lakers['Tweet'].str.contains(i, case=False)].index
    lakers.drop(remove_index, inplace = True)

#cleaning
remove_query('vicente')

#prep for export
lakers.sort_values('Date', inplace=True)
lakers = lakers.reset_index(drop=True)
#export
lakers.to_csv('../data/tweets/lakers/lakers_cleaned_tweets.csv')
