# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 01:58:29 2021

@author: -
"""

# %% imports
import requests 
import pandas as pd
import seaborn as sns

# %% scrape tables with pandas
url='https://www.covers.com/sport/football/ncaaf/printsheet'
table = pd.read_html(url)
games = table[2]
games.columns = games.iloc[8]
cgames = pd.DataFrame()
cgames = cgames.append([games[3:6], games[9:17], games[20:28], games[31:121]], ignore_index=True)
# make the rotation number the index
cgames.index = cgames['Gm#']
del cgames['Gm#']







#%%
121, 29.
18
7
2