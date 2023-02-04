from random import random
from constants import *

starting_positions = [1, 2, 3, 4, 5]

class Player():
	def __init__(self, name="", starting_position=None):
		self.name = name
		""" if starting_position is None:
			self.set_starting_position()
		else:
			self.positions = [starting_position] """
		self.set_starting_position()
		## kartice su redom TAX, BUS, UDG, RVR, X2
		self.cards = [0] * 5
	
	def move(self, vehicle, position, moves, game):
		if position in moves:
			self.positions.append(position)
			self.cards[vehicle] -= 1
			if isinstance(self, Detective):
				game.mrx.cards[vehicle] += 1
		else:
			print(moves)
			raise Exception(f"{idx_to_vehicle[vehicle]} {position} is not a legal move for {self.name}!")

	def set_starting_position(self):
		self.positions = [starting_positions[int(random() * len(starting_positions))]]
	
	def set_cards(self):
		pass

	def reset(self):
		self.set_starting_position()
		self.set_cards()
		


class Detective(Player):
	def __init__(self, name="", starting_position=None):
		super(Detective, self).__init__(name, starting_position)
		self.set_cards()
	
	def set_cards(self):
		self.cards[0] = DETECTIVE_TAX
		self.cards[1] = DETECTIVE_BUS
		self.cards[2] = DETECTIVE_UDG


class MrX(Player):
	def __init__(self, name="", starting_position=None):
		super(MrX, self).__init__(name, starting_position)
	
	def set_cards(self):
		self.cards[0] = MRX_TAX
		self.cards[1] = MRX_BUS
		self.cards[2] = MRX_UDG
		self.cards[3] = MRX_RVR
		self.cards[4] = MRX_X2


def main():
	d1 = Player()
	mrx = MrX()
	print(d1.positions[0], mrx.positions[0], starting_positions)


if __name__ == '__main__':
	main()
