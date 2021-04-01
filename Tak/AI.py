# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 02:45:12 2021

@author: carra
"""

class AI:
    
    def __init__(self, color): 
        self.color= color
        self.piecesused= 0
        self.capStoneUsed = False
        self.points =0
        
    def setPoint(self, value):
        self.points = value
        
        
    def addPoint(self):
        self.points+=1
    
    def getPoints(self):
        return self.points
    
    def getColor(self):
        return self.color
    
    def getCapStoneUsed(self):
        return self.capStoneUsed
        
    def addPiece(self):
        self.piecesused+=1
    
    def addCapStone(self):
        self.capStoneUsed = True
    
        
    def getPiecesUsed(self):
        if (self.capStoneUsed):
            return self.piecesused+1
        else:
            return self.piecesused
        