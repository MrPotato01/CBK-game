import pygame

class Menu():
    def windoww(self, menu, start, exit, hun):
        menu.fill((255, 51, 51))

        #draw buttons
        if start.draw(menu) == True: #if the returned value from the draw function (action) is true /// WIN is the surface var from button file
            print("Start button clicked")
        if exit.draw(menu) == True: #WIN is the surface var from button file
            print("exit button clicked")
            hun[0] = False