import pygame
from player import Player
from ball import Ball
from settings import WIDTH, HEIGHT, player_width, player_height

class Table:
	def __init__(self, screen):
		self.screen = screen
		self.game_over = False
		self.score_limit = 7
		self.ball = Ball(WIDTH // 2 - player_width, HEIGHT - player_width, player_width)
		self._generate_world()

	# create and add player to the screen
	def _generate_world(self):
		self.playerA = Player(0, HEIGHT // 2 - (player_height // 2), player_width, player_height)
		self.playerB = Player(WIDTH - player_width,  HEIGHT // 2 - (player_height // 2), player_width, player_height)

	def _ball_hit(self):
		# print(self.playerA.rect.left, self.playerB.rect.right)
		if self.ball.rect.right >= WIDTH:
			self.ball.rect.x = WIDTH // 2
		elif self.ball.rect.left <= 0:
			self.ball.rect.x = WIDTH // 2

		if pygame.Rect.colliderect(self.ball.rect, self.playerA.rect):
			self.ball.direction = "right"
			print(True)
		if pygame.Rect.colliderect(self.ball.rect, self.playerB.rect):
			self.ball.direction = "left"

	def player_move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			if self.playerA.rect.top > 0:
				self.playerA.move_up()
		if keys[pygame.K_s]:
			if self.playerA.rect.bottom < HEIGHT:
				self.playerA.move_bottom()

		if keys[pygame.K_UP]:
			if self.playerB.rect.top > 0:
				self.playerB.move_up()
		if keys[pygame.K_DOWN]:
			if self.playerB.rect.bottom < HEIGHT:
				self.playerB.move_bottom()


	def update(self):		
		self.playerA.update(self.screen)		
		self.playerB.update(self.screen)
		self.ball.update(self.screen)
		self._ball_hit()
