import copy
from constants import *


class Board():
	def __init__(self, tax_filename="", bus_filename="", udg_filename="", rvr_filename=""):
		tax = self.read_board(tax_filename)
		bus = self.read_board(bus_filename)
		udg = self.read_board(udg_filename)
		## rvr kao river
		rvr = self.read_board(rvr_filename)
		self.boards = [tax, bus, udg, rvr]
		## dodati x2
		## !!!!!!!!!
		self.legal_moves = {position: [self.get_legal_moves(vehicle_idx, position) for vehicle_idx in range(4) if position in self.boards[vehicle_idx]] for position in range(1, MAX_STATION + 1)}
		for position in range(1, MAX_STATION + 1):
			self.legal_moves[position][3] = list(set(self.legal_moves[position][0] + self.legal_moves[position][1] + self.legal_moves[position][2] + self.legal_moves[position][3]))
		# for position in range(1, MAX_STATION + 1):
		# 	self.initialize_legal_moves_x2(position)

	def read_board(slef, filename):
		## A dictionary is 6.6 times faster than a list when we lookup in 100 items.
		## https://towardsdatascience.com/faster-lookups-in-python-1d7503e9cd38

		max_station = MAX_STATION + 1
		board = {index: [] for index in range(1, max_station)}
		
		with open(filename, 'r') as f:
			for line in f:
				## removes trailing charactes (eg. '\n', ' ')
				line = line.rstrip()
				[start, end] = list(map(int, line.split()))
				board[start].append(end)
				board[end].append(start)
		
		return board
	
	def get_legal_moves(self, vehicle_idx, position):
		return self.boards[vehicle_idx][position]
	
	def initialize_legal_moves_x2(self, position):
		# print(self.legal_moves[position])
		# legal_moves = copy.deepcopy(self.legal_moves)
		legal_moves = self.legal_moves
		x2 = copy.deepcopy(legal_moves[position][:-1])
		# x2 = [[self.get_legal_moves(player, move) for move in vehicle] for vehicle in x2]
		x2 = [[legal_moves[move] for move in vehicle] for vehicle in x2]
		print(f"x: {x2}")
		self.legal_moves[position].append(x2)


def main():
	tax_filename = "tax.txt"
	bus_filename = "bus.txt"
	udg_filename = "udg.txt"
	rvr_filename = "rvr.txt"
	board = Board(tax_filename, bus_filename, udg_filename, rvr_filename)
	print(board.legal_moves)

if __name__ == '__main__':
	main()