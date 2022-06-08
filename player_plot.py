# -*- coding: utf-8 -*-
"""
Created on Mon May 23 03:39:32 2022

@author: robin
"""

import pybaseball as pyb
from pybaseball import spraychart, statcast_batter
pyb.cache.enable()

#%%
fname = input('what player? (first name): ')
lname = input('what player? (last name): ')
dd = pyb.playerid_lookup(lname,fname)
mlbam = int(dd['key_mlbam'].values)
df=statcast_batter(start_dt='2022-05-01',end_dt='2022-05-23',player_id=mlbam)
sub = df
spraychart(sub, 'generic', colorby='events')
