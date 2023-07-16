import pygame, sys
from settings import WIDTH, HEIGHT

pygame.init()

class Ball:
	def __init__(self, x, y, radius, length = 0):
		self.x = x
		self.y = y
		self.radius = radius
		self.length = length
		self.color = pygame.Color("red")
		self.direction = "right"
		self.serve = False
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
		if self.y >= HEIGHT - self.radius:
			self.speed_y = -20
		elif self.y <= 0 + self.radius:
			self.speed_y = 20

		# wall bounce handling

		self.x += self.speed_x
		self.y += self.speed_y


	def update(self, screen):
		self._ball_movement()
		ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.length)
