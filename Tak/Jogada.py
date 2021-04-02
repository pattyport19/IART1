# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 03:20:28 2021

@author: carra
"""

class Jogada:
    def __init__(self, SinglePlay, board, usedCap): 
        self.singlePlay= SinglePlay
        self.board= board
        self.usedCap = usedCap
        
    def getSinglePlay(self):
        return self.singlePlay
        