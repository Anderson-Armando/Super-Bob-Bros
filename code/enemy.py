import pygame 
from tiles import AnimatedTile
from random import randint


class Enemy(AnimatedTile):
	def __init__(self, size, x, y, actual_level):
		if actual_level == 0:
			super().__init__(size, x, y, '../graphics/enemy/run')
			self.rect.y += size - self.image.get_size()[1]
			self.speed = randint(3, 5)
		elif actual_level == 1:
			super().__init__(size, x, y, '../graphics/enemy/run1')
			self.rect.y += size - self.image.get_size()[1]
			self.speed = randint(3, 5)

		elif actual_level == 2:
			super().__init__(size, x, y, '../graphics/enemy/run2')
			self.rect.y += size - self.image.get_size()[1]
			self.speed = randint(3, 5)

	def move(self):
		self.rect.x += self.speed

	def reverse_image(self):
		if self.speed > 0:
			self.image = pygame.transform.flip(self.image, True, False)

	def reverse(self):
		self.speed *= -1

	def update(self, shift):
		self.rect.x += shift
		self.animate()
		self.move()
		self.reverse_image()