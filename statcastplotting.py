# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:08:36 2022

@author: robin
"""
#%%imports and init data collections
import pybaseball as pyb, seaborn as sns, matplotlib.pyplot as plt, datetime as dt
pyb.cache.enable()
today = dt.datetime.today().isoformat()[:10]
season = pyb.statcast('2022-04-01',today)
season=season.dropna(axis=1,how='all')

#%%set variables
ip = season[season['type']=='X']
non = season[season['type']!='X']
ev = ['single','double','triple','home_run']
hits = season.query('events=="single" or events=="double" or events=="triple" or events=="home_run"')
strikes = non[non['type']=='S']
ball = non[non['type']=='B']
st_fastballs=strikes.query('pitch_name=="4-Seam Fastball" or pitch_name=="Cutter" or pitch_name=="Sinker" or pitch_name=="Fastball" or pitch_name=="Split-Finger"')
st_offspeed=strikes.query('pitch_name=="Curveball" or pitch_name=="Changeup" or pitch_name=="Slider" or pitch_name=="Knuckle Curve" or pitch_name=="Eephus"')

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
# ax=sns.catplot(x='bb_type', y='hit_distance_sc', hue='events',col='stand', data=hits)
# ax.set(ylabel='Hit Distance (ft)', xlabel="")

ax=sns.catplot(x='events', y='launch_angle', hue='estimated_woba_using_speedangle', data=hits)
ax.set(ylabel='Hit Distance (ft)', xlabel="")

# ax=sns.kdeplot(x='launch_angle', y='hit_distance_sc', hue='events',col='stand', data=hits)
# ax.set(ylabel='Hit Distance (ft)', xlabel="launch angle in degrees")
#%%
sns.stripplot(x='bb_type', y='launch_speed',hue='woba_value', data=hits)

#%%
df = pyb.teams()
df = df[df['yearID']>=2022]
corr_mat = df.corr().stack().reset_index(name="correlation")
#%%
sns.relplot(x='launch_angle',y='launch_speed',hue='events',style='bb_type',palette='Set1',data=hits)