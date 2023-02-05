import numpy as np
from constants import *
from board import Board
from player import Detective, MrX
from game import Game
from simulation import Simulation

class Node():

    def __init__(self, game, ind, parent_ind):
        self.positions = [player.position for player in game.players]
        self.cards = [player.cards for player in game.players]
        self.wins = 0
        self.losses = 0
        self.visits = 0
        self.legal_moves = game.get_legal_moves(player=game.players[game.turn])
        self.children = []
        self.ind = ind
        self.parent_ind = parent_ind
        self.is_terminal = game.is_over()

        self.nodes_expanded = False

class MCTS():

    def __init__(self, num_iters):
        self.tree = [] * (num_iters + 1)

    def UCB1(self, node):
        ret = []
        for ind in node.children:
            temp = self.tree[ind]
            if temp.visits == 0:
                ret.append(123456789)
                continue
            ret.append( temp.wins / temp.visits + C_PARAMETER * (np.log(node.visits) / temp.visits) ) #UCB1 formula
        return ret

    def selection(self, node):
        while True:
            if node.nodes_expanded == False:
                return node
            if len(node.children):
                selected_ind = np.argmax(self.UCB1(node))
                node = self.tree[node.children[selected_ind]]
                continue
            break
        return node

    def expansion(self, node):
        pass

    def simulation(self):
        pass

    def backpropagation(self):
        pass

    def create_root_node(self):
        pass

    def search(self):
        pass

def main():
    board = Board("tax.txt", "bus.txt", "udg.txt", "rvr.txt")
        
        
    d1 = Detective("Detective 1")
    d2 = Detective("Detective 2")
    mrx = MrX("Mr. X")

    detectives = [d1, d2]
    game = Game(detectives, mrx, board)
    game.turn = 0

    node = Node(game, 1, 0)
    print(node.legal_moves)

if __name__ == '__main__':
    main()