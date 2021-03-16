# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:34:57 2021

@author: carra
"""


class Player:
    
    def __init__(self, color): 
        self.color= color
        self.piecesused= 0
        self.capStoneUsed = False
        
    def addPiece(self):
        self.piecesused+=1
    
    def addCapStone(self):
        self.capStoneUsed = True
        
    def getPiecesUsed(self):
        if (self.capStoneUsed):
            return self.piecesused+1
        else:
            return self.piecesused
        