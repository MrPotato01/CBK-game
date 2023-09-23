# In pygame, (0.0) is the top left corner of the screen

import pygame
import button
import menu

import time
import random

#Window
WIDTH, HEIGHT = 1530, 770 #Window width and height
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Display the window with width and height /// WIN is also the surface var from the button file
pygame.display.set_caption("The CBK World") #Window Title

#images - Main Menu
start_img = pygame.image.load("start_btn.png").convert_alpha() #what is convert alpha shit?
exit_img = pygame.image.load("exit_btn.png").convert_alpha()
#images - Inside the game
BG = pygame.image.load("gg.jpg")
#BG = pygame.transform.scale(pygame.image.load("Intro.jpg"),(WIDTH, HEIGHT)) #to scale the img into the window size

#Create buttons instances
start_button = button.Button(350, 300, start_img)
exit_button = button.Button(900, 300, exit_img)

def main():
    run = [True]

    while run[0]:
        menu.Menu.windoww(0, WIN, start_button, exit_button, run)  # Main menu settings

        #for loop of the window
        for event in pygame.event.get(): #checking for events happeing while running
            if event.type == pygame.QUIT: #if the exit button of the window clicked then:
                run[0] = False
                break #as no reason to continue checking the events after pressing the quit button
        pygame.display.update()
    pygame.quit() #Exit the window/game

if __name__ == "__main__": #this make sure that you call the main() from this file and not importing it from anywhere else ?!!
    main()