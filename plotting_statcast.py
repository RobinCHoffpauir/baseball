# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:58:39 2022

@author: robin
"""

import pandas as pd
from pybaseball import schedule_and_record

teams = ['BOS','NYY','TBR','TOR','BAL','CLE','MIN','KC','CHW',
         'DET','HOU','LAA','SEA','TEX','OAK','WSN','MIA','ATL',
         'NYM','PHI','CHC','MIL','STL','PIT','CIN','LAD','ARI',
         'COL','SD','SF']

# collect every team's record for the 2018 season
records = []
for t in teams:
    s = schedule_and_record(2021, t)
    records.append(s)

#concatenate records together so the whole season is in one dataframe
df = pd.concat(records, axis = 0)

# standardize the date formats of double-header games
df.Date = df.Date.str.replace(' (1)','',regex=False)
df.Date = df.Date.str.replace(' (2)','',regex=False)

# turn this into a date format that Pandas will recognize
df.Date = pd.to_datetime(df.Date,format='%A, %b %d')
df.Date = df.Date.map(lambda x: x.replace(year=2018))

# cut out games that havent happened yet
df = df.loc[df.Date < '2018-08-05']

# extract win and loss values from "w-l" strings
df['W'] = df['W-L'].str.split('-').str[0].astype(int)
df['L'] = df['W-L'].str.split('-').str[1].astype(int)
df['win_pct'] = df['W'] / (df['W'] + df['L'])

df.to_csv('2018-records.csv')
#%%
team_colors ={'BOS' : '#BD3039', 'NYY' : '#003087', 'TBR' : '#8FBCE6', 'KCR' : '#BD9B60', 'CHW' : '#27251F', 'BAL' : '#DF4601', 'CLE' : '#E31937', 'MIN' : '#002B5C', 'DET' : '#FA4616', 'HOU' : '#EB6E1F', 'LAA' : '#BA0021', 'SEA' : '#005C5C', 'TEX' : '#003278', 'OAK' : '#003831', 'WSN' : '#14225A', 'MIA' : '#FF6600', 'ATL' : '#13274F', 'NYM' : '#002D72', 'PHI' : '#E81828', 'CHC' : '#0E3386', 'MIL' : '#B6922E', 'STL' : '#C41E3A', 'PIT' : '#FDB827', 'CIN' : '#C6011F', 'LAD' : '#005A9C', 'ARI' : '#A71930', 'COL' : '#33006F', 'SDP' : '#002D62', 'SFG' : '#FD5A1E', 'TOR' : '#134A8E'}
