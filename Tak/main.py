# -*- coding: utf-8 -*-
"""3
Created on Sun Mar 14 16:05:04 2021

@author: carra
"""

import tak



def main():
    """
    game = tak.Tak(3)
    game.place(2,1)
    game.place(2,0)
    game.placeCap(2,0)

    #game.placeWall(2,2)
    game.display()
    game.nextPosMoves(game.board, game.current)    

    
    
    v2
    
    game= tak.Tak(3)
    game.switch()
    game.place(1,1)
    game.placeCap (2,2)
    game.place(2,0)
    game.place(1,0)
    game.switch()
    """
    game= tak.Tak(3)
    game.switch()
    game.place(1,1)
    game.placeCap (2,2)
    game.place(2,1)
    game.place(1,2)
    game.switch()

    temp= True
    while temp :
        
        game.play()
            
        game.display()
        if (game.checkFinished(game.current, game.board)):
            print("Player Isla Won!")
            return True
        
        game.switch()

        game.aiBestMove()
        game.display()
        if (game.checkFinished(game.current, game.board)):
            print("Player AI Won!")
            return True
        game.switch()
        

        
    
        yes= input("quer jogar mais ?y(yes) n(no)")
        if (yes == "n"):
            temp= False


         
    
main()