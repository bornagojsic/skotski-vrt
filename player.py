from random import random
from copy import deepcopy
from constants import *

starting_positions = [103, 112, 34, 155, 94, 117, 132, 53, 174, 198, 50, 91, 26, 29, 141, 13, 138, 197]

class Player():
	def __init__(self, name="", starting_position=None, taken_positions=None):
		self.name = name
		if starting_position is None:
			self.set_starting_position(taken_positions)
		else:
			self.positions = [starting_position]
		self.set_starting_position()
		## kartice su redom TAX, BUS, UDG, RVR
		self.cards = [0] * 4
		self.set_cards()
	
	def move(self, vehicle, position, moves, game):
		if position in moves:
			self.position = position
			self.cards[vehicle] -= 1
			if isinstance(self, Detective):
				game.mrx.cards[vehicle] += 1
		else:
			print(moves)
			print(self.cards)
			print(game.get_moves_by_vehicle(self, vehicle))
			print(self.position)
			print(game.board.legal_moves)
			raise Exception(f"{idx_to_vehicle[vehicle]} {position} is not a legal move for {self.name}!")

	# def set_starting_position(self, taken_positions=None):
	# 	if taken_positions is None:
	# 		taken_positions = TAKEN_POSITIONS
	# 	# input(taken_positions)
	# 	while True: #Makes sure two players can't start at the same spot
	# 		self.position = starting_positions[int(random() * len(starting_positions))]
	# 		if not taken_positions[self.position]: 
	# 			taken_positions[self.position] = 1
	# 			break
	
	def set_cards(self):
		if isinstance(self, Detective):
			self.cards = deepcopy(DETECTIVE_CARDS)
		else:
			self.cards = deepcopy(MRX_CARDS)

	def reset(self):
		self.set_starting_position()
		self.set_cards()
		


class Detective(Player):
	def __init__(self, name="", starting_position=None):
		super(Detective, self).__init__(name, starting_position)


class MrX(Player):
	def __init__(self, name="", starting_position=None):
		super(MrX, self).__init__(name, starting_position)

def main():
	d1 = Detective()
	mrx = MrX()
	print(d1.position, mrx.position, starting_positions)
	print(d1.cards, mrx.cards)


if __name__ == '__main__':
	main()
