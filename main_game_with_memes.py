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

#Powerups active or inactive
another = False
awful = False
future = False
blur = False
stump = False
force = False
jokie = False
doit = False
snappa = False
comb = False
rekt = False
sleep = False
spoder = False
card = False
lift = False
taxes = False

#Dictionary with Powerup Image filenames
memes = {0:"Another one.JPG", 1:"Awful-Memes2.jpg", 2:"bernie for the future.jpg", 3:"blurrr.jpg", \
		4:"Cant stump the Trump.jpg", 5:"feel the force.jpg", 6:"OH SNAPPA.jpg", 7:"Over comb.jpg", \
		8:"rekt.jpg", 9:"sleep.jpg", 10:"spoderman.jpg", 11:"trump card.png", 12:"uevenliftbro.jpg", 13:"UNLIMITED TAXES.jpg"}

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
	speed = 15

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		i = random.randint(0, 13)
		#generates random powerup

		self.image = pygame.image.load("Memes/" + memes[1])
		#opens image file for corresponding powerup
		
		self.rect = self.image.get_rect()
		screen.blit(self.image, (self.xPos, self.yPos))

	def update(self):
		self.yPos += self.speed
		screen.blit(self.image, (self.xPos, self.yPos))
		#Powerup object moves down screen

class Bullet(pygame.sprite.Sprite):
	#Initialize bullet values
	size = (10, 4)
	speed = 3

	def __init__(self):
		#Creates sprite and draws bullet
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(self.size)
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x -= self.speed

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
		"""if keys[K_LEFT]:
			if(self.xPos > 0):
				self.xPos -= self.speed
		if keys[K_RIGHT]:
			if(self.xPos < xScreen - self.size[0]):
				self.xPos += self.speed"""

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

#Creates window
screen = pygame.display.set_mode((xScreen, yScreen))

#Adds things to groups so they can all be calculated and updated at once
sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
blocks = pygame.sprite.Group()

def powerup(player, enemy, bullet):
	global damage
	global bps
	bps = 40 if another else 2

	global awful
	bps = 1 if awful else 2
	player.speed = 1 if awful else 2

	global future
	bps = 45 if future else 2
	player.speed = 4 if future else 2

	#global blur
	
	global stump
	if stump and player.health > 50:
		player.health = 50 

	global force
	bullet.speed = 6 if force else 2
	bullet.size = (20, 20) if force else (4, 4)

	#global jokie
	#global doit

	global snappa
	if snappa:
		for i in range(0, 10):
			blocks.remove(blocks[i])
			sprites.remove(blocks[i])

	global comb
	if comb:
		for i in range(0,yScreen/Block.size[1]):
			row4 = Block()
			row4.rect.x = xScreen/3+Block.size[0] * 2
			row4.rect.y = row4.size[1]*i
			blocks.add(row4)
			sprites.add(row4)

	global wait
	#Counter used for powerups that immobilize/ have a time element

	global rekt
	if rekt:
		player.speed = 0
		wait += 1
		if wait >= fps * 3:
			rekt = False
	else:
		player.speed = 2

	global sleep
	if sleep:
		for enemy in enemies:
			enemy.speed = 0;
		wait += 1
		if wait >= fps * 3:
			rekt = False
	else:
		enemy.speed = 2

	global spoder
	if spoder:
		for block in blocks:
			block.hit += 1

	global card
	if card:
		for i in range(0,yScreen/Block.size[1]):
			row4 = Block()
			row4.rect.x = xScreen/3+Block.size[0] * 2
			row4.rect.y = row4.size[1]*i
			blocks.add(row4)
			sprites.add(row4)

	#If we can figure out how to implement this powerup
	'''global lift
	if lift:
		bullet.rect.y -= bullet.speed
	else:
	'''

	global taxes
	if taxes:
		bullet.size = (20, 20)
		bullet.speed = 6
		bps = 40
		damage = 2
	else:
		bullet.size = (4, 4)
		bullet.speed = 3
		bps = 2
		damage = 1


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
						bullet = Bullet()

						#Check for powerup
						powerup(player, enemy, bullet)
						
						bullet.rect.x = player.rect.x
						bullet.rect.y = player.rect.y+player.size[1]/2
						sprites.add(bullet)
						bullets.add(bullet)

						#Refreshes cooldown
						cooldown = 0

		global wait
		if wait >= fps * 10:
			power = Power_up()
			sprites.add(power)
			wait = 0
		else:
			wait += 1

		#Refresh every object's position
		sprites.update()
		

		#Checks if bullet collides with block, removes block/bullet on collision or screen exit
		for bullet in bullets:
			hit = pygame.sprite.spritecollide(bullet, blocks, False)

			for block in hit:
				bullets.remove(bullet)
				sprites.remove(bullet)
				#Add one hit to block
				block.hit += damage
				#Check if block is broken
				if(block.hit >= durability):
					blocks.remove(block)
					sprites.remove(block)

			if bullet.rect.x < 0:
				bullets.remove(bullet)
				sprites.remove(bullet)

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

main()