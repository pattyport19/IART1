# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:33:19 2021

@author: carra
"""
class Heuristica:
    def __init__(self): 
        #margem que estamos a procura
         self.margemx0 = False
         self.margemxn = False
         self.margemy0 = False
         self.margemyn = False
         self.margem = True
    
     
    def setmargemx0 (self):
         self.margemx0 = True
     
        
    def setmargemxn (self):
         self.margemxn = True
         
    def setmargemy0 (self):
         self.margemy0 = True
        
        
    def setmargemyn (self):
         self.margemyn = True
        
    def priority1(self):
        return (self.margemx0|self.margemyn|self.margemxn|self.margemy0)
    
             