import pygame, sys
from pygame.locals import *

pygame.init()

width = 800 #default width 
height = 600 #default height
#can change if needed

black = (0, 0, 0)
gray = (169, 169, 169)
white = (255, 255, 255)
#colors that I used for main menu

backgroundImg = pygame.image.load("trumpwall.png")
#backgroundRect = backgroundImg.get_rect()


gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Trump's Border Patrol") #change later for actual game name
clock = pygame.time.Clock()

pause = False

def text_objects(text, font): #for black colored text
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font): #for white colored text
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects2(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
    
def paused():
    while pause:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white) #or whatever background colow you guys want
        largeText = pygame.font.Font("freesansbold.ttf", 50)
        TextSurf, TextRect = text_objects("Paused", largeText) 
        TextRect.center = ((width/2), (height/4))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue", 267, 250, 300, 60, black, gray, unpause )
        button("Quit", 267, 400, 300, 60, black, gray, quitgame)

        pygame.display.update()
        clock.tick(15)
    
def main_menu():
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white) #or whatever background color you guys want
        gameDisplay.blit(backgroundImg, (0,0))
        
        largeText = pygame.font.Font("freesansbold.ttf", 50)
        TextSurf, TextRect = text_objects("Trump's Border Patrol", largeText) #change game name later 
        TextRect.center = ((width/2), (375))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start", 150, 450, 200, 60, black, gray, game_loop)
        button("Quit", 450, 450, 200, 60, black, gray, quitgame)

        pygame.display.update()
        clock.tick(15)
    
def game_loop(): #this should with the rest of the game code also
    global pause
    crashed = False #if cancel button clicked (x)
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN: #if button pressed
                if event.key == pygame.K_p: #if p key hit, paused 
                    pause = True
                    paused()

        pygame.display.update()
        clock.tick(60)

main_menu()
game_loop()
pygame.quit()
quit()
