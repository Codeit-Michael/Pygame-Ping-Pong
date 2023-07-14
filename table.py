import pygame
from player import Player
from settings import WIDTH, HEIGHT, player_width, player_height

class Table:
	def __init__(self, screen):
		self.screen = screen
		self.game_over = False
		self.score_limit = 7
		self._generate_world()

	# create and add player to the screen
	def _generate_world(self):
		self.playerA = Player(0, HEIGHT // 2 - (player_height // 2), player_width, player_height)
		self.playerB = Player(WIDTH - player_width,  HEIGHT // 2 - (player_height // 2), player_width, player_height)

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
