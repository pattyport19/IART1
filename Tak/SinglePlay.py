# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:15:38 2021

@author: carra
"""


class SinglePlay:   

   def __init__(self): 
        self.x = None
        self.y = None
        self.direction = None
        self.distance = None
        self.player = None
        
   def getDirection(self):
       return self.direction
   
   def getX(self):
       return self.x
   
   def getY(self):
       return self.y
   
   def getDistance(self):
       return self.distance
   
   def getPlayer(self):
       return self.player
   
   def initials(self,x,y):
       self.x =x
       self.y = y
   
   def setDirection(self, direction):
       self.direction = direction
       
   def setDistance (self, distance):
       self.distance = distance
   
   def setPlayer(self, player):
       self.player= player
       
       
   def place(self, x, y, player):
      self.x = x
      self.y = y
      self.direction = None
      self.distance = None
      self.player = player
      
       
   def move(self, x, y , direction, distance):
      self.x = x
      self.y = y
      self.direction = direction
      self.distance = distance
       
       

