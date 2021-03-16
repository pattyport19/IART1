# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:05:04 2021

@author: carra
"""

import tak



def main():
    counter=0
    game= tak.Tak()
    while (counter<5):
        counter+=1
        
        x = int(input('Please enter x pos: '))
        y= int(input('Please enter y value: '))
        w= input("Please enter if piece type (n(normal),w(wall), t(top))")
        
        if (w== "w"):
            game.placeWall(x,y)
        elif (w== "t"):
            game.place(x,y)
        else:
            game.place(x,y)
        game.switch()
        game.display()
    
main()