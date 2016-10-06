#Status for the user
import pygame
import sys
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)


class status(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 30)
        #self.screen = pygame.display.set_mode((1280,720), 0, 32)
        #self.screen.fill((black))

        #draw rectangle for the status
        self.addRect(0, 540, 426, 180)
        self.addRect(426, 540, 426, 180)
        self.addRect(852, 540, 428, 180)

        self.addText("HP:", 70, 600)
        self.addText("Power up:", 500, 580)
        self.addText("Boss HP:", 960+30, 600)
        
        pygame.display.update()

    def addRect(self, x, y, length, width):
        self.rect = pygame.draw.rect(self.screen, (white), (x, y, length, width), 2)
        pygame.display.update()

    def addText(self, text, x, y):
        self.screen.blit(self.font.render(text, True, white), (x, y))
        pygame.display.update()        

    def hpStatus(self,hp):
        #set default as 100 for now, will work on to reduce HP later
        return str(hp)

    def weaponPowerUp(self, weapon):
        return weapon
    
    def update(self):
        #update the status of the player
        self.addRect(0, 540, 426, 180)
        self.addRect(426, 540, 426, 180)
        self.addRect(852, 540, 428, 180)

        self.addText("HP:", 70, 600)
        self.addText("Power up:", 500, 580)
        self.addText("Boss HP:", 960+30, 600)

        self.addText(hpStatus(Player.health))
        self.addText(hpStatus(Enemy.health))
        #self.addText(self.weaponbPowerUp())
