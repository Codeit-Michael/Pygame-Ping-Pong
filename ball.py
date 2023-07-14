import pygame, sys
from settings import WIDTH, HEIGHT

pygame.init()

class Ball:
	def __init__(self, x, y, radius, length = 0):
		self.x = x
		self.y = y
		self.color = pygame.Color("red")
		self.radius = radius
		self.length = length
		self.status = "fall"
		self.FPS = pygame.time.Clock()
		self.dir = 10

	def animate(self, screen):
		if self.y >= HEIGHT - self.radius:
			self.status = "bounce"
		elif self.y <= 0 + self.radius:
			self.status = "fall"

		if self.x >= WIDTH - self.radius:
			self.dir = -50
		elif self.x <= 0 + self.radius:
			self.dir = 50

		if self.status == "fall":
			self.y += 20
			self.x += self.dir
		else:
			self.y -= 20
			self.x += self.dir

		if self.x >= WIDTH + self.radius // 2:
			self.x = 0 - self.radius // 2


		ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.length)
