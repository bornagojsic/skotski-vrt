from random import shuffle
from constants import *

starting_positions = [1, 2, 3, 4, 5]

class Player():
	def __init__(self, name="", starting_position=None):
		self.name = name
		if starting_position is None:
			shuffle(starting_positions)
			self.positions = [starting_positions.pop()]
		else:
			self.positions = [starting_position]
		## kartice su redom TAX, BUS, UDG, RVR, X2
		self.cards = [0] * 5
	
	
	def move(self, vehicle, position, moves, game):
		if position in moves[vehicle]:
			self.positions.append(position)
			self.cards[vehicle] -= 1
			if isinstance(self, Detective):
				game.mrx.cards[vehicle] += 1
		else:
			raise Exception(f"{idx_to_vehicle[vehicle]} {position} is not a legal move for {self.name}!")


class Detective(Player):
	def __init__(self, name="", starting_position=None):
		super(Detective, self).__init__(name, starting_position)
		self.cards[0] = DETECTIVE_TAX
		self.cards[1] = DETECTIVE_BUS
		self.cards[2] = DETECTIVE_UDG


class MrX(Player):
	def __init__(self, name="", starting_position=None):
		super(MrX, self).__init__(name, starting_position)
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