#!/usr/bin/python

#package battingPackage
import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from teamPackage import Pitcher
from teamPackage import Player

class CurrentBatting(object):

    def __init__(self, pitcher, player):
        self.strikes = 0
        self.fouls = 0
        self.balls = 0
        self.homerunOrWalk = ""
        self.pitcher = pitcher
        self.player = player

    def add_Strike(self):
        self.strikes = self.strikes + 1

    def add_Ball(self):
        self.balls = self.balls + 1

    def add_Foul(self):
        self.fouls = self.fouls + 1

    def get_Strikes(self):
        return self.strikes

    def set_Strikes(self, strikes):
        self.strikes = strikes

    def get_Balls(self):
        return self.balls

    def set_Balls(self, balls):
        self.balls = balls;

    def get_Fouls(self):
        return self.fouls;

    def set_Fouls(self, fouls):
        self.fouls = fouls

    def get_Player(self):
        return self.player

    def get_Pitcher(self):
        return self.pitcher

    def getHomerunOrWalk(self):
        return self.homerunOrWalk

    def setHomerunOrWalk(self, homerunOrWalk):
        self.homerunOrWalk = homerunOrWalk
