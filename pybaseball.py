python
# In[4]:


import pybaseball as pyb, pandas as pd, seaborn as sns
pyb.cache.enable()


# In[14]:


df=pyb.statcast('2021-04-01','2021-06-01')


# In[6]:


x


# In[33]:



sns.relplot(x='launch_angle', y='hit_distance_sc', hue='bb_type', data=df)


# In[7]:


x.columns


# In[15]:


x = x[x['type']=='X']

