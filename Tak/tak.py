# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:23:13 2021

@author: carra
"""
import Player
import SinglePlay
import HeuristicaFim


     


##fazer funcoes de verificacao
##fazer a ideia da capstone
     

class Tak:
     def __init__(self, size): 
        self.size=size
        self.board = [[[] for j in range(size)] for i in range(size)]
        self.Player1= Player.Player("B")
        self.Player2= Player.Player("W")
        self.current= self.Player1
        self.lastPlay = SinglePlay.SinglePlay()
        
       
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
             else:
                 break
         x= xinitial
         y= yinitial
         
 
         if (move=="m"): 
             counter =0
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
                         for j in range(len(pieces)):
                             self.board[yinitial][x].append(pieces.pop())
                         print("invalid move")
                         return False
                     while (len(pieces)>0):
                         print(pieces)
                         self.display()
                         if(self.verifyNeighboard(y,x-1)):
                             if (len(pieces) ==1):
                                 if (xinitial == x): #a casa escolhida so tem 1 peca
                                     self.board[yinitial][xinitial-1].append(pieces.pop())
                                     self.lastPlay.move(yinitial,xinitial, direction, 1)
                                     return True
                                 else: # so restou uma peca para jogar
                                     self.board[yinitial][x].append(pieces.pop())
                                     self.lastPlay.move(yinitial,xinitial, direction,counter)
                                     return True
                                     
                                 
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
                                 if (yes == maxi):
                                    self.lastPlay.move(yinitial,xinitial, direction,counter)
                                    return True
                                 counter+=1
                         else:  #aqui o neighboard ja morreu 
                             if (pieces[0]== "CB" or pieces[0] == "CW"):
                                if (self.verifyIfCap(yinitial,x-1)):  ##caso em que posso mexer a capstone
                                     if (len(pieces)==1): #so esta a cap stone no pieces
                                         self.moveCapStone(yinitial,x-1, pieces[0])
                                         self.lastPlay.move(yinitial,xinitial, direction,counter+1)
                                         return True
                                         
                                    
                                     mini=0
                                     maxi= len(pieces)
                                     while(True):
                                        yes = int(input('How many pieces would you like to drop?: '))
                                        if (yes >=mini and yes <= maxi):
                                            break
                                     if (yes == maxi):              # estao a cap stone e + pieces mas quero deixar tudo
                                        for j in range(len(pieces)):
                                            self.board[yinitial][x].append(pieces.pop())
                                        self.lastPlay.move(yinitial,xinitial, direction,counter)
                                        return True
                                     else:    # estao a cap stone e + pieces e quero mexer a cap stone
                                         for j in range(len(pieces)-1):
                                            self.board[yinitial][x].append(pieces.pop())  
                                         self.moveCapStone( yinitial,x-1, pieces[0])
                                         self.lastPlay.move(yinitial,xinitial, direction,counter+1)
                                         return True
                                else: #caso em que nao posso mexer nem com a cap stone
                                    for j in range(len(pieces)):
                                        self.board[yinitial][x].append(pieces.pop())
                                    
                                    
                                    if (xinitial== x):                                     
                                        print("invalid move, pick something else")
                                        return False
                                    else:  
                                        self.lastPlay.move(yinitial,xinitial, direction,counter)
                                        return True
                                                                        
                                    
                             else:  #se a peça no topo nao for a cap e o neighboard falhou
                                 for j in range(len(pieces)):
                                        self.board[yinitial][x].append(pieces.pop())
                                    
                                 if (xinitial== x):                                     
                                        print("invalid move, pick something else")
                                        return False
                                 else:
                                     self.lastPlay.move(yinitial,xinitial, direction,counter)
                                     return True
                                 
                                
                 elif(direction == "s"):
                     isla= False
                     if (y>=self.size-1):
                         for j in range(len(pieces)):
                             self.board[yinitial][x].append(pieces.pop())
                         print("invalid move")
                         return False
                     while (len(pieces)>0):
                         print(pieces)
                         self.display()
                         print(y+1,x)
                         if(self.verifyNeighboard(y+1,x)):
                             if (len(pieces) ==1):
                                 if (yinitial == y):
                                     self.board[yinitial+1][xinitial].append(pieces.pop())
                                     self.lastPlay.move(yinitial,xinitial, direction, 1)
                                     return True
                                 else:
                                     self.board[y][xinitial].append(pieces.pop())
                                     self.lastPlay.move(yinitial,xinitial, direction,counter)
                                     return True
                                     
                                 
                             else:
                                 if (yinitial == y):
                                     mini =0
                                     maxi= len(pieces)-1
                                 else:
                                     mini =1
                                     maxi= len(pieces)
                                     
                                 while(True):
                                     yes = int(input('How many pieces would you like to drop?: '))
                                     if (yes >=mini and yes <= maxi):
                                         break
                                 for j in range(yes):
                                    self.board[y][xinitial].append(pieces.pop())
                                 y+=1
                                 if (yes == maxi):
                                    self.lastPlay.move(yinitial,xinitial, direction,counter)
                                    return True
                                 counter+=1
                         else:
                             if (pieces[0]== "CB" or pieces[0] == "CW"):
                                if (self.verifyIfCap(y+1,xinitial)):
                                     if (len(pieces)==1):
                                         self.moveCapStone(y+1,xinitial, pieces[0])
                                         self.lastPlay.move(yinitial,xinitial, direction,counter+1)
                                         return True
                                         
                                    
                                     mini=0
                                     maxi= len(pieces)
                                     while(True):
                                        yes = int(input('How many pieces would you like to drop?: '))
                                        if (yes >=mini and yes <= maxi):
                                            break
                                     if (yes == maxi):
                                        for j in range(len(pieces)):
                                            self.board[y][xinitial].append(pieces.pop())
                                        self.lastPlay.move(yinitial,xinitial, direction,counter)
                                        return True
                                     else:
                                         for j in range(len(pieces)-1):
                                            self.board[y][xinitial].append(pieces.pop())  
                                         self.moveCapStone( y+1,xinitial, pieces[0])
                                         self.lastPlay.move(yinitial,xinitial, direction,counter+1)
                                         return True
                                else:
                                    for j in range(len(pieces)):
                                        self.board[y][xinitial].append(pieces.pop())
                                    
                                    
                                    if (yinitial== y):                                     
                                        print("invalid move, pick something else")
                                        return False
                                    else:
                                        self.lastPlay.move(yinitial,xinitial, direction,counter)
                                        return True
                                                                        
                                    
                             else: 
                                 for j in range(len(pieces)):
                                        self.board[y][xinitial].append(pieces.pop())
                                    
                                 if (yinitial== y):                                     
                                        print("invalid move, pick something else")
                                        return False
                                 else:
                                     self.lastPlay.move(yinitial,xinitial, direction,counter)
                                     return True
                     
                 elif(direction == "d"):
                     isla= False
                     if (x>=self.size-1):
                         for j in range(len(pieces)):
                             self.board[yinitial][x].append(pieces.pop())
                         print("invalid move")
                         return False
                     while (len(pieces)>0):
                         print(pieces)
                         self.display()
                         if(self.verifyNeighboard(y,x+1)):
                             if (len(pieces) ==1):
                                 if (xinitial == x):
                                     self.board[yinitial][xinitial+1].append(pieces.pop())
                                     self.lastPlay.move(yinitial,xinitial, direction, 1)
                                     return True
                                 else:
                                     self.board[yinitial][x].append(pieces.pop())
                                     self.lastPlay.move(yinitial,xinitial, direction, counter)
                                     return True
                                     
                                 
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
                                 if (yes == maxi):
                                    self.lastPlay.move(yinitial,xinitial, direction,counter)
                                    return True
                                 counter+=1
                         else:
                             if (pieces[0]== "CB" or pieces[0] == "CW"):

                                if (self.verifyIfCap(yinitial,x+1)):

                                     if (len(pieces)==1):
                                         self.moveCapStone(yinitial,x+1, pieces[0])
                                         self.lastPlay.move(yinitial,xinitial, direction,counter+1)
                                         return True

                                    
                                     mini=0
                                     maxi= len(pieces)
                                     while(True):
                                        yes = int(input('How many pieces would you like to drop?: '))
                                        if (yes >=mini and yes <= maxi):
                                            break
                                     if (yes == maxi):
                                        for j in range(len(pieces)):
                                            self.board[yinitial][x].append(pieces.pop())
                                        self.lastPlay.move(yinitial,xinitial, direction,counter)
                                        return True
                                     else:
                                         for j in range(len(pieces)-1):
                                            self.board[yinitial][x].append(pieces.pop())  
                                         self.moveCapStone( yinitial,x+1, pieces[0])
                                         self.lastPlay.move(yinitial,xinitial, direction,counter+1)                                         
                                         return True
                                else:
                                    for j in range(len(pieces)):
                                        self.board[yinitial][x].append(pieces.pop())
                                    
                                    if (xinitial== x):                                     
                                        print("invalid move, pick something else")
                                        return False
                                    else:
                                        self.lastPlay.move(yinitial,xinitial, direction,counter)
                                        return True
                                                                        
                                    
                             else: 
                                 for j in range(len(pieces)):
                                        self.board[yinitial][x].append(pieces.pop())
                                    
                                 if (xinitial== x):                                     
                                        print("invalid move, pick something else")
                                        return False
                                 else:
                                     self.lastPlay.move(yinitial,xinitial, direction,counter)
                                     return True
                        
                                  
                     
                 elif(direction == "w"):
                     isla= False
                     print(y)
                     if (y<0):
                         for j in range(len(pieces)):
                             self.board[yinitial][x].append(pieces.pop())
                         print("invalid move")
                         return False
                     while (len(pieces)>0):
                         print(pieces)
                         self.display()
                         if(self.verifyNeighboard(y-1,x)):
                             if (len(pieces) ==1):
                                 if (yinitial == y):
                                     self.board[yinitial-1][xinitial].append(pieces.pop())
                                     self.lastPlay.move(yinitial,xinitial, direction, 1)
                                     return True
                                 else:
                                     self.board[y][xinitial].append(pieces.pop())
                                     self.lastPlay.move(yinitial,xinitial, direction, counter)
                                     return
                                     
                                 
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
                                 if (yes == maxi):
                                    self.lastPlay.move(yinitial,xinitial, direction,counter)
                                    return True
                                 counter+=1
                         else:
                             if (pieces[0]== "CB" or pieces[0] == "CW"):

                                if (self.verifyIfCap(y-1,xinitial)):
                                     if (len(pieces)==1):
                                         self.moveCapStone(y-1,xinitial, pieces[0])
                                         self.lastPlay.move(yinitial,xinitial, direction,counter+1)
                                         return True
                                         
                                    ##make for only one piece
                                    
                                     mini=0
                                     maxi= len(pieces)
                                     while(True):
                                        yes = int(input('How many pieces would you like to drop?: '))
                                        if (yes >=mini and yes <= maxi):
                                            break
                                     if (yes == maxi):
                                        for j in range(len(pieces)):
                                            self.board[yinitial][x].append(pieces.pop())
                                        self.lastPlay.move(yinitial,xinitial, direction,counter)
                                        return True
                                     else:
                                         for j in range(len(pieces)-1):
                                            self.board[yinitial][x].append(pieces.pop())  
                                         self.moveCapStone( y-1,xinitial, pieces[0])
                                         self.lastPlay.move(yinitial,xinitial, direction,counter+1)      
                                         return True
                                else:
                                    for j in range(len(pieces)):
                                        self.board[y][xinitial].append(pieces.pop())
                                    
                                    if (yinitial== y):                                     
                                        print("invalid move, pick something else")
                                        return False
                                    else:
                                        self.lastPlay.move(yinitial,xinitial, direction,counter)
                                        return True
                                                                        
                                    
                             else: 
                                 for j in range(len(pieces)):
                                        self.board[y][xinitial].append(pieces.pop())
                                    
                                 if (yinitial== y):                                     
                                        print("invalid move, pick something else")
                                        return False
                                 else:
                                     self.lastPlay.move(yinitial,xinitial, direction,counter)
                                     return True        
                        
                             
         elif (move=="p"):
            w= input("Please enter if piece type (n(normal),w(wall), c(cap))")
        
            if (w== "w"):
                if (self.placeWall(x,y)==0):
                    self.lastPlay.place(x,y)
                    return True
                    
            elif (w== "c"):
                if (self.placeCap(x,y)==0):
                    self.lastPlay.place(x,y)
                    return True
                    
            else:
                if(self.place(x,y)==0):
                    self.lastPlay.place(x,y)
                    return True
            return False
             

         
         
         
     def verifyIfCap(self,ypos, xpos):
        if (self.board[ypos][xpos][-1]== "WB" or self.board[ypos][xpos][-1]== "WW"):
            return True
        else:
            return False
                           
                 
     def moveCapStone(self,ypos,xpos, piece):
        if (self.board[ypos][xpos][-1] == "WB"):
            self.board[ypos][xpos][-1]= "FB"
        if( self.board[ypos][xpos][-1] == "WW"):      
            self.board[ypos][xpos][-1]= "FW"
        self.board[ypos][xpos].append(piece)
        
                
        
            
     def verifyNeighboard(self,ypos,xpos): #verifies if a piece can moved to the position
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
            print(ypos, xpos)
            self.board[ypos][xpos].append("F"+self.current.color)
            self.current.addPiece()
            return 0
        else:
            return -1
    
    
     def placeCap(self, xpos, ypos):
        if not self.board[ypos][xpos]:
            self.board[ypos][xpos].append("C"+self.current.color)
            self.current.addCapStone()
            return 0
        else:
            return -1
         
         

    
     
     def checkFinished(self):  
         if (self.current.getPiecesUsed()<self.size):
             return False
         
         if (self.path()):
             self.countPoints()
             return True
         
         if (self.Player1.getPiecesUsed()>22 or self.Player2.getPiecesUsed()>22 ):
             self.countPoints()
             return True
         if not self.checkForEmpty():
             self.countPoints()
             return True
         
         return False
         
         
             
             
         
     def countPoints(self):
         self.Player1.setPoint(0)
         self.Player2.setPoint(0)
         for i in range (self.size):
             for j in range(self.size):
                 if (len(self.board[i][j])==0):
                     continue
                 else:
                     if (self.board[i][j][-1][-1] == "W" and self.board[i][j][-1][0] != "W"):
                         self.Player2.addPoint()
                     else:
                         self.Player1.addPoint()
                         
                     
                     
                     
         
     def checkForEmpty(self):
         for i in range(self.size):
             for j in range(self.size):
                 if (len(self.board[i][j]) ==0):
                     return True
            
         return False
                     
         
         
         
         
         
     def path(self): ##funcao baseada em greedy Algorithm
         self.nosAVisitar.clear()
         self.nosVisitados.clear()
         if (self.lastPlay.getDirection() == None): #caso em que o jogador fez place
             x = self.lastPlay.getX()
             y = self.lastPlay.getY()
             return self.verifyFromHere(y,x)  #mudei aqui !!!!!!!
         else: ##caso da jogada ser move
             return self.verifyFromRange()
         
            
     
     def verifyCorner(self,x ,y):
         #yesX0= False
         #yesY0= False
         #yesXn= False
         #yesYn= False
         if (x ==0):
             for i in range (self.size):
                 if (len(self.board[self.size][i]) >0):
                     if (self.board[self.size][i][-1][-1] == self.current.getColor()):
                         yesX0 = True
                         break
             if (yesX0):
                 return 1
                 #implementar greedy que tenta chegar a 
         return 0  
                         
         
     nosVisitados=[]
     nosAVisitar=[]
     
     def verifyFound(self,h, x, y):
         if (h.margemx0):
             if (x ==0):
                 return True
         if (h.margemxn):
             if (x == self.size-1):
                 return True
         if (h.margemy0):
            if (y ==0):
                return True
         if (h.margemyn):
             if (y == self.size-1):
                 return True
             
         return False
         
     #returns id of next picked node
     def heuristicPick(self, nosAVisitar, h ):
         if (h.priority1()):  ##if one of the higher priorities is True
             counterx0 =1000000
             counterxn = 100000
             counteryn = 1000000
             countery0 = 10000000
             if (h.margemx0):
                 for i in range (len(nosAVisitar)):
                     if (nosAVisitar[i][0] ==0):
                         return i
                     else:
                         if (counterx0 > nosAVisitar[i][0]):
                             counterx0 = nosAVisitar[i][0]
                             if (counterx0 < counterxn and counterx0 < countery0 and counterx0 < counteryn):
                                pick = i         
             if (h.margemxn):
                 for i in range (len(nosAVisitar)):
                     if (nosAVisitar[i][0] == self.size-1 ):
                         return i
                     else:
                         if (counterxn > self.size - nosAVisitar[i][0]-1):
                             counterxn = self.size - nosAVisitar[i][0] -1
                             if (counterxn < counterx0 and counterxn < countery0 and counterxn < counteryn):
                                pick = i      
             if (h.margemy0):
                for i in range (len(nosAVisitar)):
                     if (nosAVisitar[i][1] ==0):
                         return i
                     else:
                         if (countery0 > nosAVisitar[i][1]):
                             countery0 = nosAVisitar[i][1]
                             if (countery0 < counterxn and countery0 < counterx0 and countery0 < counteryn):
                                pick = i         
             if (h.margemyn):
                 for i in range (len(nosAVisitar)):
                     if (nosAVisitar[i][1] == self.size-1 ):
                         return i
                     else:
                         if (counteryn > self.size - nosAVisitar[i][1]-1):
                             counteryn = self.size - nosAVisitar[i][1] -1
                             if (counteryn < counterx0 and counteryn < countery0 and counteryn < counterxn):
                                pick = i  
             return pick
         else: #pick the node closer to a border
             counter= 100000000
             for i in range (len(nosAVisitar)):
                 for j in range(2):  
                     temp = nosAVisitar[i][j]
                     if (self.size -temp -1 < temp):
                         temp = self.size -temp -1
                     if (counter > temp):
                         counter = temp
                         pick = i
                         if (counter == 0 ):
                             return pick
             return pick
                         

            
     def checkNodeValid(self, x, y):
         me = [x,y]
         print(me)
         if (me in self.nosVisitados):
             return False  ##False
         if (len(self.board[x][y]) <=0):  #put it back when its done
            return False
         if (self.board[x][y][-1][-1] != self.current.color):  
             return False  #False
         if (self.board[x][y][-1][1] == "W"):  ##check if this is working
             return False  #False
         return True  #True 
        
     def addAdjNodes(self, xinitial ,yinitial ):
        if (xinitial > 0):
             no = [xinitial-1, yinitial]
             if (self.checkNodeValid(xinitial-1, yinitial)):
                 self.nosAVisitar.append(no)
        if (yinitial >0):
             no = [xinitial, yinitial-1]
             if (self.checkNodeValid(xinitial, yinitial-1)):
                 self.nosAVisitar.append(no)
        if (xinitial < self.size-1):
             no = [xinitial +1 , yinitial]
             if (self.checkNodeValid(xinitial+1, yinitial)):
                 self.nosAVisitar.append(no)
        if (yinitial < self.size-1):
             no = [xinitial, yinitial +1]
             if (self.checkNodeValid(xinitial, yinitial+1)):
                 self.nosAVisitar.append(no)
    

     def evolveHeuristic(self,xinitial, yinitial, h):
         if(xinitial == 0 ):
             h.setmargemxn()
         if(xinitial == self.size -1):
             h.setmargemx0()
         if(yinitial == 0 ):
             h.setmargemyn()
         if(yinitial == self.size -1):
             h.setmargemy0()  
         
         return h

               
     def greedy(self, xinitial, yinitial, h):
         self.nosVisitados.append([xinitial,yinitial])
          #adds any new priorities that might arive         
         
         if (self.verifyFound(h, xinitial, yinitial)):
             return True
         h = self.evolveHeuristic(xinitial, yinitial, h)
         self.addAdjNodes(xinitial, yinitial)
         while(len(self.nosAVisitar) >0):
                 pick = self.heuristicPick(self.nosAVisitar, h)
                 coord = self.nosAVisitar.pop(pick)
                 if (self.greedy(coord[0], coord[1], h)):
                     return True
        
         return False
                
                 
                 
         
         
         
         
     def verifyFromHere(self,xinitial, yinitial):
         h = HeuristicaFim.Heuristica()
         
         
         if (xinitial == 0 ):
             if (yinitial == 0):
                 h.setmargemxn()
                 h.setmargemyn()
                 return self.greedy(xinitial, yinitial, h)
                 # corner 0x0
                 
                 
             elif (yinitial == self.size):
                 h.setmargemxn()
                 h.setmargemy0()
                 return self.greedy(xinitial, yinitial, h)
                 #corner 0xn
                 
             else: #just an edge
                 h.setmargemxn()
                 return self.greedy(xinitial, yinitial, h)
                 
         elif (xinitial == self.size-1):
             if (yinitial == 0):
                 h.setmargemx0()
                 h.setmargemyn()
                 return self.greedy(xinitial, yinitial, h)
                 # corner nx0
             elif (yinitial == self.size):
                 h.setmargemx0()
                 h.setmargemy0()
                 return self.greedy(xinitial, yinitial, h)
                 #corner nxn
             else: #just an edge
                 h.setmargemx0()
                 return self.greedy(xinitial, yinitial, h)
         elif (yinitial == self.size-1):  ##just edge yn
             h.setmargemy0()
             return self.greedy(xinitial, yinitial, h)
         
         elif (yinitial == 0): #just edge y0
             h.setmargemyn()
             return self.greedy(xinitial, yinitial, h)
        
         else: #middle  #greedy sem objectivo algum
            return self.greedy(xinitial, yinitial, h)
            #if (self.board[xinitial +1][yinitial])
            
            
        
         
     def display(self):
         print(self.board[0])
         print(self.board[1])
         print(self.board[2])         
         
         
     def switch(self):
        if (self.current == self.Player1):
            self.current= self.Player2
        else:
            self.current= self.Player1
    
    

        
            
         
                    
        
        
        
    