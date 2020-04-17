import numpy as np
import pandas as pd
import glob

#create dataframe with all csvs in this folder concatenated
knicks = pd.concat([pd.read_csv(f, index_col=0) for f in glob.glob('../data/tweets/knicks/raw/*.csv')], ignore_index = True)
#datetime conversion
knicks['Date'] = pd.to_datetime(knicks['Date'])
EST = pd.Timedelta('5 hours')
knicks['Date'] = knicks['Date'] - EST
#remove hyperlinks
knicks['Tweet'] = knicks['Tweet'].str.replace('\w+:\/\/\S+', '', case=False)
#drop duplicate tweets
knicks = knicks.drop_duplicates('Tweet')
#reset index
knicks.reset_index(drop=True, inplace=True)
#export raw concatted csv
knicks.to_csv('../data/tweets/knicks/knicks_tweets_concat_raw.csv')

#remove query function
def remove_query(i):
    remove_index = knicks[knicks['Tweet'].str.contains(i, case=False)].index
    knicks.drop(remove_index, inplace = True)

#cleaning
remove_query('sr ')
remove_query('director')

#prep for export
knicks.sort_values('Date', inplace=True)
knicks = knicks.reset_index(drop=True)
#export
knicks.to_csv('../data/tweets/knicks/knicks_cleaned_tweets.csv')
