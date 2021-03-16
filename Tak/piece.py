# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 18:40:47 2021

@author: carra
"""

from enum import Enum
class Color(Enum):
     Black = 0
     White = 1
     
class Conf(Enum):
    flatStone=0
    wallStone=1
    capStone= 2
    
    
    

class Piece:   

   def __init__(self, color, conf): 
        self.color = color
        self.conf = conf
        
        
   def display(self):
      print(self.color)
      
   def changeToWall(self):
       self.conf = Conf.wallStone


       