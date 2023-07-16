import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		super().__init__()
		self.x = x
		self.y = y
		self.rect = pygame.Rect(self.x, self.y, width, height)
		self.color = pygame.Color("gray")
		self.player_speed = 15
		
		self.score = 0

	def move_up(self):
		self.rect.y -= self.player_speed

	def move_bottom(self):
		self.rect.y += self.player_speed

	def update(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)