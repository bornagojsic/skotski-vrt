import matplotlib.pyplot as plt
import numpy as np
from constants import *
from board import Board
from player import Detective, MrX
from game import Game

class Simulation():
    def __init__(self):
        self.mrx_wins = 0
        self.det_wins = 0

    def play_random(self, game):
        player = game.players[game.turn]
        if (sum(player.cards) == 0):
            return

        #Chooses a random move
        moves = game.get_legal_moves(player)
        rnd1 = np.random.randint(0, 4)
        while len(moves[rnd1]) == 0: #Can't pick a move when there are no moves to pick with that vehicle
            rnd1 = np.random.randint(0, 4)
        
        rnd2 = np.random.randint(0, len(moves[rnd1]))
        position = moves[rnd1][rnd2]
        vehicle = rnd1

        game.make_move(player, vehicle, position)

        game.turn += 1
        game.turn %= len(game.players)
        if (game.turn == 0):
            game.round += 1 

    def simulate_game(self, game):
        while not game.is_over():
            self.play_random(game)
        
        if (game.round >= MAX_ROUNDS):
            self.mrx_wins += 1
        else:
            self.det_wins += 1
        return

    def play_n_randoms(self, n):
        for i in range (n):
            board = Board("tax.txt", "bus.txt", "udg.txt", "rvr.txt")

            d1 = Detective("Detective 1")
            d2 = Detective("Detective 2")
            mrx = MrX("Mr. X")
            detectives = [d1, d2]

            game = Game(detectives, mrx, board)
            self.simulate_game(game)
            print(i, "Mr. X wins:", self.mrx_wins, "Detectives wins:", self.det_wins)

    def make_chart(self):
        plt.pie([self.mrx_wins, self.det_wins], labels=["Mr. X wins", "Detectives wins"])
        plt.show()


def main():
    n = int(input())
    sim = Simulation()
    sim.play_n_randoms(n)
    sim.make_chart()

if __name__ == '__main__':
    main()