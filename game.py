import copy
from constants import *
from board import Board
from player import Detective, MrX


class Game():
	def __init__(self, detectives, mrx, board):
		self.detectives = detectives
		self.mrx = mrx
		self.players = detectives + [mrx]
		self.board = board
		self.turn = 0
		self.round = 1
		print(board.boards)
	
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
		print(f"{player.name} possible moves: {get_possible_moves(player, self)}, cards: {player.cards}")
	
	def play(self):
		player = self.players[self.turn]
		if (sum(player.cards) == 0):
			return

		## nacin inputa -> "vrsta transportacije" "nova pozicija"
		## npr: TAX 1
		player_move = input(f"{player.name} move: ")
		[vehicle, position] = player_move.split()
		position = int(position)
		vehicle = vehicle_to_idx[vehicle]
		# print(f"\n\n{vehicle}, {position}\n\n")
		make_move(player, vehicle, position, self)

		self.turn += 1
		self.turn %= len(self.players)
		if (self.turn == 0):
			self.round += 1


def get_moves_by_vehicle(player, vehicle_idx, game):
	boards = copy.deepcopy(game.board.boards)
	# print(boards)
	possible_moves = []
	if player.cards[vehicle_idx]:
		possible_moves = boards[vehicle_idx][player.positions[-1]]
	# print("\n", vehicle_idx, possible_moves)
	for detective in game.detectives:
		detective_position = detective.positions[-1]
		# print("dp:", detective_position, end="")
		if detective_position in possible_moves:
			possible_moves.remove(detective_position)
	return possible_moves


def get_possible_moves(player, game, position=None):
	if position is None:
		tax = get_moves_by_vehicle(player, 0, game)
		bus = get_moves_by_vehicle(player, 1, game)
		udg = get_moves_by_vehicle(player, 2, game)
		if isinstance(player, MrX):
			rvr = get_moves_by_vehicle(player, 3, game)
			rvr = list(set(tax + bus + udg + rvr))
		else:
			rvr = []
		x2 = []
		if isinstance(player, MrX):
			if (player.cards[4]):
				## treba implementirat
				## !!!!!!!!!!!!!!!!!!!
				x1 = [tax, bus, udg, rvr]
				# for move in x1:
				# 	get_possible_moves(player, game, move)
				x2 = []
		moves = [tax, bus, udg, rvr, x2]
		return moves
	else:
		##
		pass


def make_move(player, vehicle, position, game):
	## limitirat kretanje mrxa na polja na kojima su detektivi
	## i detektiva isto lol
	## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	moves = get_possible_moves(player, game)
	if (vehicle in range(4)):
		player.move(vehicle, position, moves, game)
	if (vehicle == 4):
		pass


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