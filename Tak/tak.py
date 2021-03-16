# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:23:13 2021

@author: carra
"""
import Player
import piece


##fazer funcoes de verificacao
##fazer a ideia da capstone

class Tak:
     def __init__(self, size): 
        self.size=size
        self.board = [[[] for j in range(size)] for i in range(size)]
        self.Player1= Player.Player("B")
        self.Player2= Player.Player("W")
        self.current= self.Player1
       
     def getPlayerPiece(self,xpos,ypos):
         return self.board[ypos][xpos][-1][-1]
         
         
         
     def play(self):
         print("Player " + self.current.color + " ")
         while True:
             move = input('Please enter what u want to play(m (move), p(place)): ')       
             xinitial = int(input('Please enter x pos: '))
             yinitial= int(input('Please enter y value: '))
             if (len(self.board[yinitial][xinitial])>0 and (self.getPlayerPiece(xinitial, yinitial) != self.current.color)):
                 print("Invalid Move, Go again")
                 return False
         x= xinitial
         y= yinitial
         
 
         if (move=="m"): 
             ##Falta destruir as paredes
             if (len(self.board[yinitial][xinitial])<1):
                 return False
                 
             
             allowed= len(self.board[yinitial][xinitial])
             pieces=[]
             
             if (allowed>= self.size):
                 allowed = self.size
             
             for i in range(allowed):
                pieces.append(self.board[yinitial][xinitial].pop())
             
            
             isla = True
             while isla:
                 direction = input('Input direction of movement(a(left), d(right), w(up), s(down)): ')
             
                 if (direction == "a"):
                     isla=False
                     if (xinitial<=0):
                         continue
                     while (len(pieces)>0):
                         print(pieces)
                         self.display()
                         if(self.verifyNeighboard(y,x-1)):
                             if (len(pieces) ==1):
                                 if (xinitial == x):
                                     self.board[yinitial][xinitial-1].append(pieces.pop())
                                     return True
                                 else:
                                     self.board[yinitial][x].append(pieces.pop())
                                     
                                 
                             else:
                                 if (xinitial == x):
                                     mini =0
                                     maxi= len(pieces)-1
                                 else:
                                     mini =1
                                     maxi= len(pieces)
                                     
                                 while(True):
                                     yes = int(input('Quantas pecas deseja deixar?: '))
                                     if (yes >=mini and yes <= maxi):
                                         break
                                 for j in range(yes):
                                    self.board[yinitial][x].append(pieces.pop())
                                 x-=1

                         else:
                             if (xinitial== x):
                                 print("invalid move, pick something else")
                                 return False
                             else:
                                 for j in range(len(pieces)):
                                    self.board[yinitial][x].append(pieces.pop())
                                 return True                       
                                 
                                
                 elif(direction == "s"):
                     isla= False
                     if (y>=self.size-1):
                         continue
                     while (len(pieces)>0):
                         print(pieces)
                         self.display()
                         if(self.verifyNeighboard(y+1,x)):
                             if (len(pieces) ==1):
                                 if (yinitial == y):
                                     self.board[yinitial+1][xinitial].append(pieces.pop())
                                     return True
                                 else:
                                     self.board[y][xinitial].append(pieces.pop())
                                     
                                 
                             else:
                                 if (yinitial == y):
                                     mini =0
                                     maxi= len(pieces)-1
                                 else:
                                     mini =1
                                     maxi= len(pieces)
                                     
                                 while(True):
                                     yes = int(input('Quantas pecas deseja deixar?: '))
                                     if (yes >=mini and yes <= maxi):
                                         break
                                 for j in range(yes):
                                    self.board[y][xinitial].append(pieces.pop())
                                 y+=1
                         else:
                             if (yinitial== y):
                                 print("invalid move, pick something else")
                                 return False
                             else:
                                 for j in range(len(pieces)):
                                    self.board[y][xinitial].append(pieces.pop())
                                 return True
                     
                 elif(direction == "d"):
                     isla= False
                     if (x>=self.size-1):
                         continue
                     while (len(pieces)>0):
                         print(pieces)
                         self.display()
                         if(self.verifyNeighboard(y,x+1)):
                             if (len(pieces) ==1):
                                 if (xinitial == x):
                                     self.board[yinitial][xinitial+1].append(pieces.pop())
                                     return True
                                 else:
                                     self.board[yinitial][x].append(pieces.pop())
                                     
                                 
                             else:
                                 if (xinitial == x):
                                     mini =0
                                     maxi= len(pieces)-1
                                 else:
                                     mini =1
                                     maxi= len(pieces)
                                     
                                 while(True):
                                     yes = int(input('Quantas pecas deseja deixar?: '))
                                     if (yes >=mini and yes <= maxi):
                                         break
                                 for j in range(yes):
                                    self.board[yinitial][x].append(pieces.pop())
                                 x+=1
                         else:
                             if (xinitial== x):
                                 print("invalid move, pick something else")
                                 return False
                             else:
                                 for j in range(len(pieces)):
                                    self.board[yinitial][x].append(pieces.pop())
                                 return True
                                  
                     
                 elif(direction == "w"):
                     isla= False
                     print(y)
                     if (y<0):
                         continue
                     while (len(pieces)>0):
                         print(pieces)
                         self.display()
                         if(self.verifyNeighboard(y-1,x)):
                             if (len(pieces) ==1):
                                 if (yinitial == y):
                                     self.board[yinitial-1][xinitial].append(pieces.pop())
                                     return True
                                 else:
                                     self.board[y][xinitial].append(pieces.pop())
                                     
                                 
                             else:
                                 if (yinitial == y):
                                     mini =0
                                     maxi= len(pieces)-1
                                 else:
                                     mini =1
                                     maxi= len(pieces)
                                     
                                 while(True):
                                     yes = int(input('Quantas pecas deseja deixar?: '))
                                     if (yes >=mini and yes <= maxi):
                                         break
                                 for j in range(yes):
                                    self.board[y][xinitial].append(pieces.pop())
                                 y-=1
                         else:
                             if (yinitial== y):
                                 print("invalid move, pick something else")
                                 return False
                             else:
                                 for j in range(len(pieces)):
                                    self.board[y][xinitial].append(pieces.pop())
                                 return True
                             
         elif (move=="p"):
            w= input("Please enter if piece type (n(normal),w(wall), c(cap))")
        
            if (w== "w"):
                self.placeWall(x,y)
            elif (w== "t"):
                self.place(x,y)
            else:
                self.place(x,y)
             
                                                        

                    
                 
     def moveCapStone(self,xpos,ypos):
        if (self.board[ypos][xpos][-1] == "WB"):
            self.board[ypos][xpos][-1]= "FB"
        if( self.board[ypos][xpos][-1] == "WW"):      
            self.board[ypos][xpos][-1]= "FW"
                
        
            
     def verifyNeighboard(self,xpos,ypos):
         if (xpos ==-1 or ypos==-1):
             return False
         if (xpos >= self.size or ypos >= self.size):
             return False
         if not self.board[ypos][xpos]:
             return True
         elif (self.board[ypos][xpos][-1] == "WB" or self.board[ypos][xpos][-1] == "WW" or self.board[ypos][xpos][-1] == "CW" or self.board[ypos][xpos][-1] == "CB"):
             return False
         else:
             return True
             
             
         
        
     def placeWall(self, xpos, ypos):
        if not self.board[ypos][xpos]:
            self.board[ypos][xpos].append("W"+self.current.color)
            self.current.addPiece()
            return 0
        else:
            return -1
        
     def place(self, xpos, ypos):
        if not self.board[ypos][xpos]:
            self.board[ypos][xpos].append("F"+self.current.color)
            self.current.addPiece()
            return 0
        else:
            return -1
    
     def placeCap(self, xpos, ypos):
        if not self.board[ypos][xpos]:
            self.board[ypos][xpos].append("C"+self.current.color)
            self.current.addPiece()
            return 0
        else:
            return -1
         
         

    
     
        
     def display(self):
         print(self.board[0])
         print(self.board[1])
         print(self.board[2])         
         
     def switch(self):
        if (self.current == self.Player1):
            self.current= self.Player2
        else:
            self.current= self.Player1
    
    

        
            
         
                    
        
        
        
    