import copy
from random import randint
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
		self.mrx_positions = []
		
	def set_state(self, positions, cards, turn, round):
		for ind, player in enumerate(self.players):
			player.position = positions[ind]
			for i in range (5):
				player.cards[i] = cards[ind][i]
		self.turn = turn
		self.round = round
	
	def reset_players(self):
		starting_positions = copy.deepcopy(STARTING_POSITIONS)
		for i in range(len(self.players)):
			self.position = starting_positions.pop(randint(0, len(starting_positions) - 1))

	def is_over(self):
		if self.round >= MAX_ROUNDS:
			return True
		
		for self.detective in self.detectives:
			if self.detective.position == self.mrx.position:
				return True
		return False
	
	def print_positions(self):
		for player in self.players:
			print(f"{player.name} positions: {player.position}")
	
	def print_moves(self):
		print("Moves: [TAX, BUS, UDG, RVR, X2]")
		player = self.players[self.turn]
		print(f"{player.name} possible moves: {self.get_legal_moves(player)}, cards: {player.cards}")
		pass
	
	def get_legal_moves(self, player, position=None):
		#If I comment this part below, it doesn't crash. Why????
		"""if (sum(player.cards)) == 0:
			return player.position"""
		tax = self.get_moves_by_vehicle(player, 0, position)
		bus = self.get_moves_by_vehicle(player, 1, position)
		udg = self.get_moves_by_vehicle(player, 2, position)
		if isinstance(player, MrX):
			rvr = self.get_moves_by_vehicle(player, 3, position)
			rvr = list(set(tax + bus + udg + rvr))
		else:
			rvr = []
		moves = [tax, bus, udg, rvr]
		return moves

	""" def get_moves_by_vehicle(self, player, vehicle_idx, position = None):
		if position is None:
			position = player.position
		boards = copy.deepcopy(self.board.boards)
		legal_moves = []
		if player.cards[vehicle_idx]:
			legal_moves = boards[vehicle_idx][position]
		for detective in self.detectives:
			detective_position = detective.position
			if detective_position in legal_moves:
				legal_moves.remove(detective_position)
		return legal_moves """
	
	def get_moves_by_vehicle(self, player, vehicle_idx, position=None):
		if player.cards[vehicle_idx] == 0:
			return []
		if position is None:
			position = player.position
		legal_moves = self.board.legal_moves[position][vehicle_idx]
		detectives_positions = [detective.position for detective in self.detectives]
		legal_moves = [move for move in legal_moves if not move in detectives_positions]
		return legal_moves
		
	
	def make_move(self, player, vehicle, position):
		moves = self.get_moves_by_vehicle(player, vehicle)
		player.move(vehicle, position, moves, self)

	def play(self):
		player = self.players[self.turn]
		if (sum(player.cards) == 0):
			return

		## nacin inputa -> "vrsta transportacije" "nova pozicija"
		## npr: TAX 1
		player_move = input(f"{player.name} move: ")
		vehicle = player_move.split()[0]
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
