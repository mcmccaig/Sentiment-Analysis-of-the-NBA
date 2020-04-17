import requests
import pandas as pd
import numpy as np

latemonths = ['october', 'november', 'december']
earlymonths = ['january', 'february', 'march', 'april', 'may', 'june']

#game by game attendance scraping
for i in latemonths:
    html_doc = requests.get(f'https://www.basketball-reference.com/leagues/NBA_2019_games-{i}.html').content
    tables = pd.read_html(html_doc)
    tables[0].to_csv(f'../data/attendance/{i}_2018_nba_attendance.csv', index=False)
for i in earlymonths:
    html_doc = requests.get(f'https://www.basketball-reference.com/leagues/NBA_2019_games-{i}.html').content
    tables = pd.read_html(html_doc)
    tables[0].to_csv(f'../data/attendance/{i}_2019_nba_attendance.csv', index=False)

#arena capacity scraping
html_doc = requests.get('https://en.wikipedia.org/wiki/List_of_National_Basketball_Association_arenas').content
tables = pd.read_html(html_doc)
tables[0].to_csv('../data/capacity/arena_capacity.csv', index=False)

#load in all months games and concatenate
df1 = pd.read_csv('../data/attendance/october_2018_nba_attendance.csv')
df2 = pd.read_csv('../data/attendance/november_2018_nba_attendance.csv')
df3 = pd.read_csv('../data/attendance/december_2018_nba_attendance.csv')
df4 = pd.read_csv('../data/attendance/january_2019_nba_attendance.csv')
df5 = pd.read_csv('../data/attendance/february_2019_nba_attendance.csv')
df6 = pd.read_csv('../data/attendance/march_2019_nba_attendance.csv')
df7 = pd.read_csv('../data/attendance/april_2019_nba_attendance.csv')
df_list = [df1,df2,df3,df4,df5,df6,df7]

#combine all seasons into one df
season_2018 = pd.DataFrame()
for i in df_list:
    season_2018 = season_2018.append(i, ignore_index=True)

#drop playoff games
playoff_index = season_2018[season_2018['Date'] == 'Playoffs'].index[0]
season_2018 = season_2018.iloc[:playoff_index]

#load in capacity data
capacity = pd.read_csv('../data/capacity/arena_capacity.csv')

#create dictionary of team and capacity
capacity_dict = dict(zip(capacity['Team(s)'], capacity['Capacity']))

#map capacity to season dataframe
season_2018['Capacity']= season_2018['Home/Neutral'].map(capacity_dict)

season_2018.to_csv('../data/attendance/full_season_2018_2019_attendance.csv')

#cleaning to team specific game attendance
def attendance_combiner(season_att, team_string, short_string):
    team_att = pd.DataFrame()
    away_mask = season_att['Visitor/Neutral'] == team_string
    home_mask = season_att['Home/Neutral'] == team_string
    team_att = team_att.append(season_att[home_mask])
    team_att = team_att.append(season_att[away_mask])
    team_att['Date'] = pd.to_datetime(team_att['Date'])
    team_att['Attend.'] = pd.to_numeric(team_att['Attend.'])
    team_att['Capacity'] = pd.to_numeric(team_att['Capacity'])
    team_att['Attendance Ratio'] = (team_att['Attend.'] / team_att['Capacity'])
    team_att = team_att.sort_values(by='Date')
    team_att = team_att.reset_index()
    one_mask = team_att['Attendance Ratio'] > 1
    team_att['Attendance Ratio'] = team_att['Attendance Ratio'].where(~one_mask, 1)
    team_att.to_csv(f'../data/attendance/teams/{short_string}_2018_2019_attendance.csv')
    return(team_att)

raptors_att = attendance_combiner(season_2018, 'Toronto Raptors', 'raptors')
lakers_att = attendance_combiner(season_2018, 'Los Angeles Lakers', 'lakers')
rockets_att = attendance_combiner(season_2018, 'Houston Rockets', 'rockets')
warriors_att = attendance_combiner(season_2018, 'Golden State Warriors', 'warriors')
knicks_att = attendance_combiner(season_2018, 'New York Knicks', 'knicks')
