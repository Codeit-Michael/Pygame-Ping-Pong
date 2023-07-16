import pygame, sys
from settings import WIDTH, HEIGHT

pygame.init()

class Ball:
	def __init__(self, x, y, radius, length = 0):
		self.x = x
		self.y = y
		self.radius = radius
		self.length = length
		self.rect = pygame.Rect(self.x, self.y, radius, radius)
		self.color = pygame.Color("red")
		self.direction = "right"
		self.speed_x = 0
		self.speed_y = 0

	def serve_ball(self):
		pass

	def _ball_movement(self):
		# horizontal handling
		if self.direction == "right":
			self.speed_x = 20
		else:
			self.speed_x = -20

		# vertical handling
		if self.rect.y >= HEIGHT - self.radius:
			self.speed_y = -20
		elif self.rect.y <= 0 + self.radius:
			self.speed_y = 20

		# wall bounce handling

		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

	def update(self, screen):
		self._ball_movement()
		# ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.length)
		pygame.draw.rect(screen, self.color, self.rect)