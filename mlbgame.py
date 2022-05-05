# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 03:53:34 2022

@author: robin
"""
import mlbgame as mlb
import pandas as pd

tt=mlb.games(2021)
dates = []
games = mlb.combine_games(tt)
#%%
for l in tt[:29]:
    for ll in range(len(l)):
        game = l[ll]
        dates.append(game.date)
        games.join(pd.DataFrame(game.nice_score(), index =0))

#%%

game = mlb.games(2021)
for z in range(len(game)):
    for zz in range(len(game[z])):
        games.append(game[z][zz].nice_score())


#%%
stats = mlbgame.player_stats(games.game_id)
for player in stats.home_batting:
    print(player)

#%%
com = zip(dates,awayteam)
com = pd.DataFrame(com,columns=['Date','Game'])
for le in range(9):
    if l[le].w_team == l[le].home_team:
        print("The " + l[le].w_team + ''+' beat the ' + l[le].l_team + " " + str(l[le].home_team_runs) + " " + "to " + str(l[le].away_team_runs))
    else:
        print("The " + l[le].w_team + ''+' beat the ' + l[le].l_team + " " + str(l[le].away_team_runs) + " " + "to " + str(l[le].home_team_runs))
