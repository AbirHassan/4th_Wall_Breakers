import pygame
from pygame.locals import *
import sys
import time
import random

#Screen width and height
xScreen = 1280
yScreen = 720

#Frames or calculations per second
fps = 90

#Bullets per second
bps = 2

#Damage done per bullet
damage = 1

#How many damage points blocks can withstand
durability = 3

#Timer
wait = 0

#Dictionary with Powerup Image filenames
memes = {0:["Another one.jpg", False], 1:["Awful-Memes2.jpg", False], 2:["bernie for the future.jpg", False], 3:["blurrr.jpg", False], \
		4:["Cant stump the Trump.jpg", False], 5:["feel the force.jpg", False], 6:["OH SNAPPA.jpg", False], 7:["Over comb.jpg", False], \
		8:["rekt.jpg", False], 9:["sleep.jpg", False], 10:["spoderman.jpg", False], 11:["trump card.jpg", False], 12:["UNLIMITED TAXES.jpg", False], 13:False}

#Various color tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (75, 75, 75)

class Power_up(pygame.sprite.Sprite):
	#Initialize Powerup position
	xPos = xScreen / 2
	yPos = 30
	speed = 5

	#generates random powerup
	i = random.randint(0, 12)
	#i = 0
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.i = random.randint(0, 12)

		#opens image file for corresponding powerup
		self.image = pygame.image.load("Memes/" + memes[self.i][0])
		
		self.rect = self.image.get_rect()
		self.rect.x = self.xPos
		self.rect.y = self.yPos
		screen.blit(self.image, (self.rect.x, self.rect.y))

	def update(self):
		self.rect.y += self.speed
		screen.blit(self.image, (self.rect.x, self.rect.y))
		#Powerup object moves down screen

class Bullet(pygame.sprite.Sprite):
	#Initialize bullet values
	size = (4, 4)
	speed = 2
	player = None
	angle = 0

	def __init__(self, player):
		#Creates sprite and draws bullet 
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(self.size)
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.player = player
		self.angle = self.player.angle

	def update(self):
		self.rect.x -= self.speed
		if self.angle != 0:
			if(self.rect.y <= yScreen and self.rect.y >= 0):
				self.rect.y -= self.angle 
			else:
				self.angle = -self.angle
				self.rect.y -= self.angle

class Block(pygame.sprite.Sprite):
	#Initialize block values
	size = (30, 30)
	hit = 0

	def __init__(self):
		#Creates sprite and draws block
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(self.size)
		self.image.fill(GRAY)
		self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
	#Initialize player values
	health = 100
	xPos = 1100
	yPos = 360
	size = (50, 50)
	speed = 2
	angle = 0

	def __init__(self):
		#Creates sprite and draws player
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(self.size)
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()

	def update(self):
		#Updates position
		self.rect.x = self.xPos
		self.rect.y = self.yPos
		self.keyPress()

	def keyPress(self):
		#Moves when button is held down continuously
		keys = pygame.key.get_pressed()
		if keys[K_UP]:
			if(self.yPos > 0):
				self.yPos -= self.speed
		if keys[K_DOWN]:
			if(self.yPos < yScreen - self.size[1]):
				self.yPos += self.speed	

		#In case we want to enable left/right movement again	
		if keys[K_LEFT]:
			self.angle -= 0.1
			#if(self.xPos > 0):
				#self.xPos -= self.speed
		if keys[K_RIGHT]:
			self.angle += 0.1
			#if(self.xPos < xScreen - self.size[0]):
				#self.xPos += self.speed

		#Escape key to quit game and program
		if keys[K_ESCAPE]:
			pygame.quit()
			sys.exit()
		
class Enemy(pygame.sprite.Sprite):
	#Initialize player values
	health = 100
	xPos = 150
	yPos = 360
	size = (50, 50)
	speed = 2
	

	def __init__(self):
		#Creates sprite and draws player
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(self.size)
		self.image.fill(RED)
		self.rect = self.image.get_rect()

	def update(self):
		#Updates position
		self.rect.x = self.xPos
		self.rect.y = self.yPos

#Initialize
pygame.init()
pygame.mixer.music.load("Sounds/TRUMP SONG.mp3")

#Creates window
screen = pygame.display.set_mode((xScreen, yScreen))
backgroundImg = pygame.image.load("trumpwall2.png")
pygame.display.set_caption("Trump's Border Patrol")

#Main Menu Functions
clock = pygame.time.Clock()
pause = False
 
#Writes text in given color
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
 
#Creates button with given parameters (message, position, size, color, action)
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
 
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen,ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen,ic, (x,y,w,h))
 
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText,WHITE)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)
 
def quitgame():
    pygame.quit()
    quit()
 
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
 
#Pause function of game
def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        screen.fill(WHITE)
        screen.blit(backgroundImg, (0,0))
 
        largeText = pygame.font.Font("freesansbold.ttf", 50)
        TextSurf, TextRect = text_objects("Trump's Border Patrol", largeText, BLACK)
        TextRect.center = ((xScreen/2), (450))
        screen.blit(TextSurf, TextRect)
        pygame.mixer.music.pause()
 
        button("Continue", 375, 530, 200, 60, BLACK, GRAY, main)
        button("Quit", 700, 530, 200, 60, BLACK, GRAY, quitgame)
 
        pygame.display.update()
        clock.tick(15)

#Actual main menu function
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        screen.fill(WHITE)
        screen.blit(backgroundImg, (0,0))
 
        largeText = pygame.font.Font("freesansbold.ttf", 50)
        TextSurf, TextRect = text_objects("Trump's Border Patrol", largeText, BLACK)
        TextRect.center = ((xScreen/2), (450))
        screen.blit(TextSurf, TextRect)
        pygame.mixer.music.play(-1)
 
        button("Start", 375, 530, 200, 60, BLACK, GRAY, main)
        button("Quit", 700, 530, 200, 60, BLACK, GRAY, quitgame)
 
        pygame.display.update()
        clock.tick(15)
 

#Adds things to groups so they can all be calculated and updated at once
sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
blocks = pygame.sprite.Group()
powerups = pygame.sprite.Group()

def powerup(player, enemy, bullet, n):
	global memes
	global damage
	global bps
	if memes[13]:
		if memes[0][1]:#another one
			bps = 40 
		if memes[1][1]:#awful memes
			bps = 1
			player.speed = 1
		if memes[2][1]:#future
			bps = 45
			player.speed = 4
		if memes[3][1]:#blur
			enemy.speed = 5
		if memes[4][1] and player.health > 50:#stump
			player.health = 50
		if memes[5][1]:#force
			bullet.speed = 6
			bullet.size = (20, 20)
		if memes[6][1]:#ohsnappa
			for i in range(0, 10):
				blocks.remove(blocks[i])
				sprites.remove(blocks[i])
		if memes[7][1]: #comb
			for i in range(0,yScreen/Block.size[1]):
				row4 = Block()
				row4.rect.x = xScreen/3+Block.size[0] * 2
				row4.rect.y = row4.size[1]*i
				blocks.add(row4)
				sprites.add(row4)
		if memes[8][1]: #rekt
			player.speed = 0
		if memes[9][1]: #sleep
			enemy.speed = 0
		if memes[10][1]: #spoder
			for block in blocks:
				block.hit += 1
		if memes[11][1]: #card
			for i in range(0,yScreen/Block.size[1]):
				row4 = Block()
				row4.rect.x = xScreen/3+Block.size[0] * 2
				row4.rect.y = row4.size[1]*i
				blocks.add(row4)
				sprites.add(row4)
		if memes[12][1]: #taxes
			bullet.size = (20, 20)
			bullet.speed = 6
			bps = 40
			damage = 2
		
	else:
		bps = 2
		damage = 1
		bullet.size = (4, 4)
		bullet.speed = 3
		enemy.speed = 2
		player.speed = 4

def main():
	#Initialize player
	player = Player()
	enemy = Enemy()
	sprites.add(player)
	sprites.add(enemy)

	#Creates rows of blocks
	for i in range(0,yScreen/Block.size[1]):
		row1 = Block()
		row1.rect.x = xScreen/3-Block.size[0]
		row1.rect.y = row1.size[1]*i
		blocks.add(row1)
		sprites.add(row1)

	for i in range(0,yScreen/Block.size[1]):
		row2 = Block()
		row2.rect.x = xScreen/3
		row2.rect.y = row2.size[1]*i
		blocks.add(row2)
		sprites.add(row2)

	for i in range(0,yScreen/Block.size[1]):
		row3 = Block()
		row3.rect.x = xScreen/3+Block.size[0]
		row3.rect.y = row3.size[1]*i
		blocks.add(row3)
		sprites.add(row3)

	#Controls FPS
	clock = pygame.time.Clock()

	#Cooldown between bullets
	cooldown = 0

	#Timer
	duration = 0
	#Loop to refresh game state
	while True:
		#Checks for input
		for event in pygame.event.get():
			#If spacebar is pressed shoot bullet
			if event.type == pygame.KEYDOWN:
				if event.key == K_SPACE:
					#Checks for cooldown
					if(cooldown >= fps):
						#Spawns bullet at player
						bullet = Bullet(player)
						bullet.rect.x = player.rect.x
						bullet.rect.y = player.rect.y+player.size[1]/2
						sprites.add(bullet)
						bullets.add(bullet)
						
						#Refreshes cooldown
						cooldown = 0

				elif event.key == K_p:
 					pause = True
 					paused()
 			elif event.type == pygame.QUIT:
 				pygame.quit()
 				quit()

 		global wait
		if wait >= fps * 10:
			power = Power_up()
			sprites.add(power)
			powerups.add(power)
			wait = 0
		else:
			wait += 1
		#Refresh every object's position
		sprites.update()

		n = 0

		#Checks if bullet collides with block, removes block/bullet on collision or screen exit
		for bullet in bullets:
			hit = pygame.sprite.spritecollide(bullet, blocks, False)
			powerhit = pygame.sprite.spritecollide(bullet, powerups, True)
			for block in hit:
				bullets.remove(bullet)
				sprites.remove(bullet)
				#Add one hit to block
				block.hit += damage
				#Check if block is broken
				if(block.hit >= durability):
					blocks.remove(block)
					sprites.remove(block)

			for power in powerhit:
				powerups.remove(power)
				sprites.remove(power)
				bullets.remove(bullet)

				global memes
				memes[13] = True
				memes[power.i][1] = True
				duration = 0
				print(memes[power.i][1])

				n = power.i

			if bullet.rect.x < 0:
				bullets.remove(bullet)
				sprites.remove(bullet)
		
			#Check for powerup
			powerup(player, enemy, bullet, n)
			if memes[13] == True:
				duration += 1
			if duration >= fps * 10:
				memes[13] = False
				memes[n][1] = False
				duration = 0
		#Draws everything after performing calculations
		screen.fill(BLACK)
		sprites.draw(screen)
		pygame.display.flip()

		#Controls FPS which is tied to speed, refresh rate, etc. (calculations per second)
		clock.tick(fps)

		#Constant changes cooldown, lower for more time between bullets (bullets per second)
		cooldown += bps

	#Quit game
	pygame.quit()

main_menu()
main()