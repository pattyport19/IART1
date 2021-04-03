# -*- coding: utf-8 -*-
"""3
Created on Sun Mar 14 16:05:04 2021

@author: carra
"""

import tak

def playerVsPlayer(game):
    game.switch()
    print("pick for your oponent")
    valid= False
    while(not valid):
            valid = game.play()
            game.display()
    #game.placeWall (2,2)
    game.switch()
    
    print("pick for your oponent")
    valid= False
    while(not valid):
            valid = game.play()
            game.display()
            
    game.switch()
    
    temp= True
    while temp :
        
        valid= False
        while(not valid):
            valid = game.play()
            game.display()
        #game.display()
        finished = game.checkFinished(game.current, game.board)
        if (finished == 1):
            print("Player", game.current.getColor(), "Won!")
            return True
        if (finished == 3):
            if (game.Player1.getPoints() > game.Player2.getPoints() ):
                print("Player", game.Player1.getColor(), "Won!")
                return True
            elif (game.Player1.getPoints() == game.Player2.getPoints()):
                print("Tie")
                return True
            else:
                print("Player", game.Player2.getColor(), "Won!")
                return True
                
        
        
        #game.nextPosMoves (game.board, game.current)
        game.switch()
        #game.aiBestMove()
        valid= False
        while(not valid):
            valid = game.play()
            game.display()
            
        finished = game.checkFinished(game.current, game.board)
        if (finished == 1):
            print("Player", game.current.getColor(), "Won!")
            return True
        if (finished == 3):
            if (game.Player1.getPoints() > game.Player2.getPoints() ):
                print("Player", game.Player1.getColor(), "Won!")
                return True
            elif (game.Player1.getPoints() == game.Player2.getPoints()):
                print("Tie")
                return True
            else:
                print("Player", game.Player2.getColor(), "Won!")
                return True
            
        game.switch()
        

        
    
        yes= input("quer jogar mais ?y(yes) n(no)")
        if (yes == "n"):
            temp= False



def playervsComputer(game):
    mini = 1
    maxi = 2
    tipo =  int(input("Oponent Random(1)? or Inteligent(2)?"))
    while(tipo < mini or tipo > maxi):
        print("invalid Choice, pick again")
        tipo = int(input("Oponent Random(1)? or Inteligent(2)?"))
        
    mini = 1
    maxi = 10
    if (tipo == 2):
        depth =  int(input("How inteligent? (tree depth)"))
        while(depth < mini or depth > maxi):
            print("invalid Choice, pick again")
            depth = int(input("How inteligent?(tree depth)"))
    
    

    print("pick for your oponent")
    valid= False
    while(not valid):
            valid = game.play()
            game.display()
    #game.placeWall (2,2)
    game.switch()
    game.aiRandom()
    
    
    temp= True
    while temp :
        game.display()
        
        valid= False
        while(not valid):
            valid = game.play()
            game.display()
            
        finished = game.checkFinished(game.current, game.board)
        if (finished == 1):
            print("Player", game.current.getColor(), "Won!")
            return True
        if (finished == 3):
            if (game.Player1.getPoints() > game.Player2.getPoints() ):
                print("Player", game.Player1.getColor(), "Won!")
                return True
            elif (game.Player1.getPoints() == game.Player2.getPoints()):
                print("Tie")
                return True
            else:
                print("Player", game.Player2.getColor(), "Won!")
                return True
        
        game.switch()

        if (tipo == 2):
           game.aiBestMove(depth)
        else:
            game.aiRandom()
            
            
        game.display()
        
        finished = game.checkFinished(game.current, game.board)
        if (finished == 1):
            print("Player", game.current.getColor(), "Won!")
            return True
        if (finished == 3):
            if (game.Player1.getPoints() > game.Player2.getPoints() ):
                print("Player", game.Player1.getColor(), "Won!")
                return True
            elif (game.Player1.getPoints() == game.Player2.getPoints()):
                print("Tie")
                return True
            else:
                print("Player", game.Player2.getColor(), "Won!")
                return True
        
        game.switch()
        

        
    
        yes= input("quer jogar mais ?y(yes) n(no)")
        if (yes == "n"):
            temp= False
    
    



def watchComputer(game):
    print("For player 1:")
    mini = 1
    maxi = 2
    tipo1 =  int(input("Random(1)? or Inteligent(2)?"))
    while(tipo1 < mini or tipo1 > maxi):
        print("invalid Choice, pick again")
        tipo1 = int(input("Oponent Random(1)? or Inteligent(2)?"))
        
    mini = 1
    maxi = 10
    if (tipo1 == 2):
        depth1 =  int(input("How inteligent? (tree depth)"))
        while(depth1 < mini or depth1 > maxi):
            print("invalid Choice, pick again")
            depth1 = int(input("How inteligent?(tree depth)"))
         
    print("")
            
    print("For player 2:")
    mini = 1
    maxi = 2
    tipo2 =  int(input("Random(1)? or Inteligent(2)?"))
    while(tipo2 < mini or tipo2 > maxi):
        print("invalid Choice, pick again")
        tipo2 = int(input("Oponent Random(1)? or Inteligent(2)?"))
        
    mini = 1
    maxi = 10
    if (tipo2 == 2):
        depth2 =  int(input("How inteligent? (tree depth)"))
        while(depth2 < mini or depth2 > maxi):
            print("invalid Choice, pick again")
            depth2 = int(input("How inteligent?(tree depth)"))
      
    #primeiras jogadas
    game.aiRandom()
    game.switch()
    game.aiRandom()
    game.display()
         
     
    temp= True
    while temp :
        
        
        if (tipo1 == 2):
           game.aiBestMove(depth1)
        else:
            game.aiRandom()
        
        game.display()
        finished = game.checkFinished(game.current, game.board)
        if (finished == 1):
            print("AI", game.current.getColor(), "Won!")
            return True
        if (finished == 3):
            if (game.Player1.getPoints() > game.Player2.getPoints() ):
                print("AI", game.Player1.getColor(), "Won!")
                return True
            elif (game.Player1.getPoints() == game.Player2.getPoints()):
                print("Tie")
                return True
            else:
                print("AI", game.Player2.getColor(), "Won!")
                return True
        
        
        game.switch()
        print("")
        print("")

        if (tipo2 == 2):
           game.aiBestMove(depth2)
        else:
            game.aiRandom()
            
            
        
        game.display()
        finished = game.checkFinished(game.current, game.board)
        if (finished == 1):
            print("AI", game.current.getColor(), "Won!")
            return True
        if (finished == 3):
            if (game.Player1.getPoints() > game.Player2.getPoints() ):
                print("AI", game.Player1.getColor(), "Won!")
                return True
            elif (game.Player1.getPoints() == game.Player2.getPoints()):
                print("Tie")
                return True
            else:
                print("AI", game.Player2.getColor(), "Won!")
                return True
        
        game.switch()
        
        

        
    
        yes= input("quer jogar mais ?y(yes) n(no)")
        if (yes == "n"):
            temp= False
    
    
            
    


def main():
    mini = 3
    maxi = 8
    size = int(input("what game size do you want to play?"))
    while(size == 7 or size < mini or size > maxi ):
        print("invalid Size")
        size = int(input("what game size do you want to play?"))
    
    game = tak.Tak(size)
    mini = 1
    maxi = 3
    tipo =  int(input("PvP?(1), PvC?(2), CvC?(3)"))
    while(tipo < mini or tipo > maxi):
        print("invalid Choice, pick again")
        tipo = int(input("PvP?(1), PvC?(2), CvC?(3)"))
        
    if (tipo == 1):
         playerVsPlayer(game)
    if (tipo == 2):
        playervsComputer(game)  ##escolher tipo de computador, escolher depth
    if (tipo == 3):
        watchComputer(game)  ##escolher tipo de computador, escolher depth
    
        
    #por a escolher a depth



         
    
main()




    
    
    
    