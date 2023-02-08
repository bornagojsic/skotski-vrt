from constants import *
from board import Board
from player import Detective, MrX
from game import Game
from mcts import Node, MCTS

class Playing():
	
	def __init__(self):
		pass

	def play_vs_mcts(self):
		num_iters = int(input("Enter number of MCTS iterations per move: "))
		board = Board("tax.txt", "bus.txt", "udg.txt", "rvr.txt")   
		d1 = Detective("Detective 1")
		d2 = Detective("Detective 2")
		d3 = Detective("Detective 3")
		d4 = Detective("Detective 4")
		mrx = MrX("Mr. X")
		detectives = [d1, d2]
		game = Game(detectives, mrx, board)
		game.turn = 0

		while not game.is_over():
			print("===================================")
			game.print_positions()
			game.print_moves()
			print("===================================")

			if game.turn == 0:
				mcts = MCTS(num_iters, game)
				best_move = mcts.search(num_iters)
				game.make_move(game.players[0], best_move[0], best_move[1])

				game.turn = (game.turn + 1) % (len(game.players))
				continue

			game.play()

	def recreate_bug(self, positions, cards, num_iters):
		board = Board("tax.txt", "bus.txt", "udg.txt", "rvr.txt")   
		d1 = Detective("Detective 1")
		d2 = Detective("Detective 2")
		d3 = Detective("Detective 3")
		d4 = Detective("Detective 4")
		mrx = MrX("Mr. X")
		detectives = [d1, d2]
		game = Game(detectives, mrx, board)
		game.turn = 0

		game.set_state(positions, cards, turn=0, round=11)
		mcts = MCTS(num_iters, game)
		mcts.search(num_iters)

def main():
	run = Playing()
	cards = [[6, 5, 6, 2, 2],
			[10, 8, 4, 0, 0],
			[10, 8, 4, 0, 0]]
	#run.recreate_bug([43, 77, 46], cards, 10000)
	run.play_vs_mcts()

if __name__ == '__main__':
	main()
