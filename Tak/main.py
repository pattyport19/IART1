# -*- coding: utf-8 -*-
"""3
Created on Sun Mar 14 16:05:04 2021

@author: carra
"""

import tak



def main():
    
    game= tak.Tak(3)

    
    temp= True
    while temp :
        game.play()
        game.display()
        if (game.checkFinished()):
            print("Player Isla Won!")
            return True
        yes= input("quer jogar mais ?y(yes) n(no)")
        if (yes == "n"):
            temp= False

        game.switch()
            
    
main()