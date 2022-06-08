# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:28:13 2022

@author: robin
"""
z = []
date = input('What days matchups are you looking for?: ')
url = 'https://www.cbssports.com/fantasy/baseball/probable-pitchers/'
x = pd.read_html(url + date + '')
for a in range(len(x)):
    for aa in x[a].values:
        z.append(aa)

