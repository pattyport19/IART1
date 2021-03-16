# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:23:13 2021

@author: carra
"""
import Player
import piece

class Tak:
     def __init__(self): 
        self.board = [[[] for j in range(5)] for i in range(5)]
        self.column = 5
        self.row = 5
        self.Player1= Player.Player("B")
        self.Player2= Player.Player("W")
        self.current= self.Player1
        
     def placeWall(self, xpos, ypos):
        if (self.board[xpos][ypos][-1] == -1):
            self.board[xpos][ypos].append(self.current.color+"W")
            self.current.addPiece()
            return 0
        else:
            return -1
        
     def place(self, xpos, ypos):
        if (self.board[xpos][ypos][-1] == -1):
            self.board[xpos][ypos].append(self.current.color)
            self.current.addPiece()
            return 0
        else:
            return -1
        
     def display(self):
         print(self.board[0])
         print(self.board[1])
         print(self.board[2])         
         print(self.board[3])
         print(self.board[4])
         
     def switch(self):
        if (self.current == self.Player1):
            self.current= self.Player2
        else:
            self.current= self.Player1
    
    

        
            
         
                    
        
        
        
    