import pygame

class Ball:
	def __init__(self, x, y, size):
		self.x = x
		self.y = y
		# make it circle
		self.rect = pygame.Rect(self.x, self.y, size, size)
		self.color = pygame.Color("red")
		self.player_speed = 3
