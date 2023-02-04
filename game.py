import copy
from constants import *
from board import Board
from player import Detective, MrX


class Game():
	def __init__(self, detectives, mrx, board):
		self.detectives = detectives
		self.mrx = mrx
		self.players = [mrx] + detectives
		self.board = board
		self.turn = 0
		self.round = 1
	
	def is_over(self):
		if self.round >= MAX_ROUNDS:
			return True
		
		for self.detective in self.detectives:
			if self.detective.positions[-1] == self.mrx.positions[-1]:
				return True
		return False
	
	def print_positions(self):
		for player in self.players:
			print(f"{player.name} positions: {player.positions}")
	
	def print_moves(self):
		print("Moves: [TAX, BUS, UDG, RVR, X2]")
		player = self.players[self.turn]
		print(f"{player.name} possible moves: {self.get_legal_moves(player)}, cards: {player.cards}")
		pass
	
	def get_legal_moves(self, player, position=None):
		tax = self.get_moves_by_vehicle(player, 0, position)
		bus = self.get_moves_by_vehicle(player, 1, position)
		udg = self.get_moves_by_vehicle(player, 2, position)
		if isinstance(player, MrX):
			rvr = self.get_moves_by_vehicle(player, 3, position)
			rvr = list(set(tax + bus + udg + rvr))
		else:
			rvr = []
		x2 = []
		if position is None and isinstance(player, MrX):
			x2 = self.get_moves_by_vehicle(player, 4, position)
			""" if (player.cards[4]):
				x2 = [tax, bus, udg, rvr]
				## list compreshensions because it's faster
				## get all legal moves for a first move for all moves using all vehicles
				x2 = [[self.get_legal_moves(player, move) for move in vehicle] for vehicle in x2]
				## the format of x2: [TAX, BUS, UDG, RVR, X2], where X2 is always empty
				## TAX, BUS, UDG and RVR contain of lists for each possible first move and
				## every of those lists contain possible second moves in the same order as x2 """
		moves = [tax, bus, udg, rvr, x2]
		return moves

	""" def get_moves_by_vehicle(self, player, vehicle_idx, position = None):
		if position is None:
			position = player.positions[-1]
		boards = copy.deepcopy(self.board.boards)
		legal_moves = []
		if player.cards[vehicle_idx]:
			legal_moves = boards[vehicle_idx][position]
		for detective in self.detectives:
			detective_position = detective.positions[-1]
			if detective_position in legal_moves:
				legal_moves.remove(detective_position)
		return legal_moves """
	
	def get_moves_by_vehicle(self, player, vehicle_idx, position=None):
		if not player.cards[vehicle_idx]:
			return []
		if position is None:
			position = player.positions[-1]
		legal_moves = self.board.legal_moves[position][vehicle_idx]
		if vehicle_idx == 4:
			## ne uzima u obzir pozicije detektiva
			## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			return legal_moves
		detectives_positions = [detective.positions[-1] for detective in self.detectives]
		legal_moves = [move for move in legal_moves if not move in detectives_positions]
		return legal_moves
		
	
	def make_move(self, player, vehicle, position):
		moves = self.get_moves_by_vehicle(player, vehicle)
		player.move(vehicle, position, moves, self)
		
	def make_move_x2(self, player, vehicles, position):
		## napraviti da radi
		## !!!!!!!!!!!!!!!!!
		moves = self.get_legal_moves(player)
		player.move(vehicles, position, moves, self)

	def play(self):
		player = self.players[self.turn]
		if (sum(player.cards) == 0):
			return

		## nacin inputa -> "vrsta transportacije" "nova pozicija"
		## npr: TAX 1
		player_move = input(f"{player.name} move: ")
		vehicle = player_move.split()[0]
		if vehicle == "X2":
			if isinstance(player, MrX):
				## dodati da radi
				## !!!!!!!!!!!!!!
				pass
			else:
				raise Exception(f"Player {player.name} can't use the X2 move!")
		else:
			[vehicle, position] = player_move.split()
			position = int(position)
			vehicle = vehicle_to_idx[vehicle]
			self.make_move(player, vehicle, position)

			self.turn += 1
			self.turn %= len(self.players)
			if (self.turn == 0):
				self.round += 1


def main():
	board = Board("tax.txt", "bus.txt", "udg.txt", "rvr.txt")

	d1 = Detective("Detective 1")
	d2 = Detective("Detective 2")
	mrx = MrX("Mr. X")
	detectives = [d1, d2]
	
	game = Game(detectives, mrx, board)

	while not game.is_over():
		print()
		game.print_positions()
		
		game.print_moves()
		
		game.play()
	print("\nGAME OVER\n")
	if (game.round >= MAX_ROUNDS):
		print("Mr. X wins!")
	else:
		print("Detectives win!")
	exit()


if __name__ == "__main__":
	main()