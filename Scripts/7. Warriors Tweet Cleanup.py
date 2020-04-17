import numpy as np
import pandas as pd
import glob

#create dataframe with all csvs in this folder concatenated
warriors = pd.concat([pd.read_csv(f, index_col=0) for f in glob.glob('../data/tweets/warriors/raw/*.csv')], ignore_index = True)
#order by date
warriors['Date'] = pd.to_datetime(warriors['Date'])
PST = pd.Timedelta('8 hours')
warriors['Date'] = warriors['Date'] - PST
#remove hyperlinks
warriors['Tweet'] = warriors['Tweet'].str.replace('\w+:\/\/\S+', '', case=False)
#drop duplicate tweets
warriors = warriors.drop_duplicates('Tweet')
#reset index
warriors.reset_index(drop=True, inplace=True)
#export raw concatted csv
warriors.to_csv('../data/tweets/warriors/warriors_tweets_concat_raw.csv')

#remove query function
def remove_query(i):
    remove_index = warriors[warriors['Tweet'].str.contains(i, case=False)].index
    warriors.drop(remove_index, inplace = True)

#cleaning
remove_query('weekend warrior')
remove_query('little warrior')
remove_query('my warrior')
remove_query('zu')
remove_query('be a warrior')
remove_query('fierce')
remove_query(' pose')
remove_query('fighters')
remove_query('renal')
remove_query('ninja')
remove_query('spa ')
remove_query('ladies')
remove_query('lady')
remove_query('ethos')
remove_query('academy')
remove_query('conclave')
remove_query('princess')
remove_query('boxing')
remove_query('mma ')
remove_query('muay')
remove_query('jiu')
remove_query('wrestl')
remove_query('pregnancy')
remove_query('capoeira')
remove_query('female')
remove_query('lacrosse')
remove_query('exposure')
remove_query('justice')
remove_query('hockey')
remove_query(' inner ')
warriors.to_csv('../data/tweets/warriors/warriors_2018_tweets_v3_cleaned_v1.csv')

# Cleaning Round 2
remove_query('workout')
remove_query('fitness')
remove_query('beauty')
remove_query('institute')
remove_query('hawaii')
remove_query('spirit')
remove_query('warrior king')
remove_query('power')
remove_query('military')
remove_query('armor')
remove_query('honor')
remove_query('pray')
remove_query('women')
remove_query('woman')
remove_query('eagle')
remove_query('snake')
remove_query('fight')
remove_query('beer')
remove_query('courage')
remove_query('alemany')
remove_query('sword')
remove_query(' mage')
remove_query('westminster')
warriors.to_csv('../data/tweets/warriors/warriors_2018_tweets_v3_cleaned_v2.csv')

# Cleaning Round 3
remove_query('spotify')
remove_query('cigars')
remove_query('road warrior')
remove_query('hyrule')
remove_query('warrior body')
remove_query('chief')
remove_query('wisdom')
remove_query('peace')
remove_query('panther')
remove_query('wounded')

def remove_query_case_true(i):
    remove_index = warriors[warriors['Tweet'].str.contains(i, case=True)].index
    warriors.drop(remove_index, inplace = True)

remove_query_case_true('God')
remove_query(' war ')
remove_query('martial')
remove_query('stanton')
remove_query('queen')
remove_query('combat')
remove_query('chakra')
remove_query('stencil')
remove_query('conditioning')
remove_query('cage')
remove_query('ufc')
remove_query('ptsd')
remove_query('winter warrior')
remove_query('beautiful')
remove_query(' hips')
remove_query('yoga')
remove_query('alien')
remove_query(' ice ')
remove_query('african')
remove_query('way of the warrior')
remove_query('movie')
remove_query('blacks')
remove_query('trump')
remove_query('object')
remove_query(' inning')
remove_query('golf')
remove_query('arthritis')
remove_query(' runs ')
remove_query('kevitch')
remove_query('scholar')
remove_query('jewish')
remove_query('album')
remove_query('woods')
remove_query('ultimate')
remove_query('ordinary')
remove_query('brave')
remove_query('pirate')
remove_query('gridiron')
remove_query('deadliest')

#prep for export
warriors.sort_values('Date', inplace=True)
warriors = warriors.reset_index(drop=True)
#export
warriors.to_csv('../data/tweets/warriors/warriors_cleaned_tweets.csv')
