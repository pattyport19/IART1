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

    
    """
    game= tak.Tak(3)
    game.switch()
    game.place(1,1)
    game.placeCap (2,2)
    game.place(2,0)
    game.place(1,0)
    game.switch()

    temp= True
    while temp :
        
        game.play()
            
        game.display()
        if (game.checkFinished()):
            print("Player Isla Won!")
            return True
        
        game.switch()

        game.ai()
        game.display()
        if (game.checkFinished()):
            print("Player AI Won!")
            return True
        game.switch()
        

        
    
        yes= input("quer jogar mais ?y(yes) n(no)")
        if (yes == "n"):
            temp= False


         
    
main()