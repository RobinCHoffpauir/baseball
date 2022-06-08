# -*- coding: utf-8 -*-
"""
Created on Mon May 23 04:11:33 2022

@author: robin
"""
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime as dt
import pybaseball as pyb
pyb.cache.enable()
global today
today = dt.today().isoformat()[:10]
data = pyb.statcast('2022-04-01', today)
global ev
ev = data[data['type']=='X']
sns.scatterplot(x='launch_speed',
                y='estimated_woba_using_speedangle', hue='bb_type', data=ev, palette='Set1')
plt.title('Est. wOBA using launch speed and angle')
plt.ylabel('Estimated wOBA')
plt.xlabel('Exit Velo (MPH)')
plt.show()
#%%
sns.scatterplot(x='launch_speed',
                y='hit_distance_sc',   hue='bb_type', data=ev, palette='Set1')
plt.title('Hit distance using exit velo')
plt.ylabel('Estimated hit distance FT(using statcast)')
plt.xlabel('Exit Velo (MPH)')
#%%
sns.scatterplot(x='launch_angle',
                y='estimated_ba_using_speedangle', hue='bb_type', data=ev, palette='Set1', legend='auto')
plt.title('Estimated Batting Avg. using launch angle')
plt.ylabel('Estimated Batting Avg. using launch angle+speed')
plt.xlabel('launch angle')

#%%
sns.scatterplot(x='launch_speed',
                y='launch_angle', hue='bb_type', data=ev, palette='Set1')
plt.title('Exit velocity and Launch Angle')
plt.ylabel('Launch Angle(degrees)')
plt.xlabel('Exit Velocity(MPH)')
