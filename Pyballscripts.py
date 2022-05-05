# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 17:06:32 2021

@author: robin
"""
import pybaseball as pyb


class Player:
    def __init__(self, fname, lname, playerid=None):
        self.fname = fname
        self.lname = lname
        self.id = playerid
        x = pyb.playerid_lookup(self.lname, self.fname)
        playerid = x['key_mlbam']
        self.id = (playerid).astype(int)
        print(self.fname, self.lname, 'playerid=', playerid.values)

    def get_player_stats(self):
        z = pyb.get_splits(self.id)
        print(z)
