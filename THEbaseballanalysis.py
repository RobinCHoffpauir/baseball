#!/usr/bin/env python
# coding: utf-8

#%%imports

import pybaseball as pyb, seaborn as sns, matplotlib.pyplot as plt, datetime as dt
pyb.cache.enable()
today = dt.datetime.today().isoformat()[:10]



#%% data collection and parsing
teams = ['BOS','NYY','TBR','TOR','BAL','CLE','MIN','KC','CHW',
         'DET','HOU','LAA','SEA','TEX','OAK','WSN','MIA','ATL',
         'NYM','PHI','CHC','MIL','STL','PIT','CIN','LAD','ARI',
         'COL','SD','SF']


df = pd.read_csv('C:/Users/robin/OneDrive/python/data/statcast_season21.csv')
df = df.drop('Unnamed: 0', axis=1) 

# seperate balls that are hit into play and all other pitches into DataFrames
in_play = df[df['type']=='X']
not_in_play= df[df['type']!='X']
hits = in_play.query('events=="single" or events == "double" or events == "triple" or events == "home_run"')
strikes = not_in_play[not_in_play['type']=='S']
balls = not_in_play[not_in_play['type']=='B']
lefty_st = strikes.query('p_throws=="L"')
righty_st = strikes.query('p_throws=="R"')
st_fastballs=strikes.query('pitch_name=="4-Seam Fastball" or pitch_name=="Cutter" or pitch_name=="Sinker" or pitch_name=="Fastball" or pitch_name=="Split-Finger"')
st_offspeed=strikes.query('pitch_name=="Curveball" or pitch_name=="Changeup" or pitch_name=="Slider" or pitch_name=="Knuckle Curve" or pitch_name=="Eephus"')
strikeouts = not_in_play.query('events=="strikeout" or events=="strikeout_double_play"')
#%% In[38]
sns.displot(x='launch_angle',y='launch_speed',data=hits, hue='events', palette='Set1')
sns.displot(x='launch_angle',y='launch_speed',data=hits, hue='events', kind='kde',fill=True,levels=5, palette='Set1')
sns.displot(x='launch_angle',y='launch_speed',hue='bb_type', kind='hist', palette='Set1',data=hits)



#%% In[43]:
sns.displot(x='launch_angle',y='hit_distance_sc',data=hits, hue='events', palette='Set1')
sns.displot(x='launch_angle',y='hit_distance_sc',data=hits, hue='events', kind='kde',fill=True,levels=5, palette='Set1')
sns.displot(x='launch_angle',y='hit_distance_sc',hue='bb_type', kind='hist', palette='Set1',data=hits)

 


#%% In[75]:
sns.displot(x='pfx_x',y='pfx_z',data=not_in_play, hue='pitch_type', palette='Set1')
sns.displot(x='pfx_x',y='pfx_z',data=not_in_play, hue='pitch_type', kind='kde',fill=True,levels=5, palette='Set1')
sns.displot(x='pfx_x',y='pfx_z',hue='pitch_type', kind='hist', palette='Set1',data=not_in_play)

#%%leftys
sns.displot(x=float('release_spin_rate'),y='release_speed',data='lefty_st', hue='pitch_type', palette='Set1')
sns.displot(x=float('release_spin_rate'),y='release_speed',data='lefty_st', hue='pitch_type', kind='kde',fill=True,levels=5, palette='Set1')
sns.displot(x=float('release_spin_rate'),y='release_speed',hue='pitch_type', kind='hist', palette='Set1',data='lefty_st')


#%%stacking plots

x=hits['launch_angle']
y=hits['launch_speed']
h=hits['events']
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x=x, y=y, hue=h, palette='Set1')
sns.histplot(x=x, y=y,hue=h,cmap="Set1")
sns.kdeplot(x=x, y=y, levels=5,hue=h, color="blue", linewidths=2)

#%%
xx=st_fastballs['release_spin_rate']
yy=st_fastballs['effective_speed']
hh=st_fastballs['zone']
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x=xx, y=yy, hue=hh, palette='Set1')
sns.histplot(x=xx, y=yy,hue=hh)
sns.kdeplot(x=xx, y=yy, levels=5,hue=hh, color="blue", linewidths=2)

#%%
x= st_fastballs['plate_x']
y= st_fastballs['plate_z']
h= st_fastballs['zone']
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x=x, y=y, hue=h, palette='Set1')
sns.histplot(x=x, y=y,hue=h)
sns.kdeplot(x=x, y=y, levels=5,hue=h, color="blue", linewidths=2)

#%%
x= strikeouts['plate_x']
y= strikeouts['plate_z']
h= strikeouts['pitch_name']
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x=not_in_play['plate_x'],y=not_in_play['plate_z'], hue=not_in_play['pitch_name'], palette='Set1')
# sns.histplot(x=x, y=y,hue=h)
sns.displot(x=x, y=y, kind='kde',levels=5,hue=h, color="blue")

#%%sswarmplot
ax=sns.stripplot(x='events', y='hit_distance_sc', hue='pitch_type',dodge=True, data=hits)
ax.set(ylabel='Hit Distance (ft)', xlabel="")

#%%
ax=sns.violinplot(x='events', y='launch_angle',dodge=True, data=hits)
ax.set(ylabel='Hit Distance (ft)', xlabel="")

#%%pointplot
ax = sns.catplot(x='events', y='launch_angle', kind='point', data=hits)
ax.set(ylabel='Launch angle (degrees)')


#%%columned catplot
ax=sns.catplot(x='bb_type', y='hit_distance_sc', hue='events',col='stand', data=hits)
ax.set(ylabel='Hit Distance (ft)', xlabel="")

#%%
ax=sns.catplot(x='events', y='launch_angle', hue='estimated_woba_using_speedangle', data=hits)
ax.set(ylabel='Hit Distance (ft)', xlabel="")

#%%
ax=sns.kdeplot(x='launch_angle', y='hit_distance_sc', hue='events',col='stand', data=hits)
ax.set(ylabel='Hit Distance (ft)', xlabel="launch angle in degrees")

#%%
sns.stripplot(x='bb_type', y='launch_speed',hue='woba_value', data=hits)

#%%

sns.relplot(in_play['launch_angle'].astype(float),in_play['hit_distance_sc'].astype(float), cmap='gnuplot')






