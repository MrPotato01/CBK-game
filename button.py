import pygame

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False #used for only one mouse click

    def draw(self, surface): #surface is the WIN var from main file
        mouse_action = False #The action of the mouse

        mouse_pos = pygame.mouse.get_pos() #Get the mouse position
        #check mouseover and clicked condition
        if self.rect.collidepoint(mouse_pos): #Getting the mouse pos to check if there is collision with the rect(button) or not
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #0 for left click, 1 for middle button, 2 for the right click
                self.clicked = True
                mouse_action = True #action is true as mouse is clicked
        if pygame.mouse.get_pressed()[0] == 0: #to enable the user to click again
            self.clicked = False
        #draw button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return mouse_action
