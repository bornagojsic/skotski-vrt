import numpy as np
from constants import *
from board import Board
from player import Detective, MrX
from game import Game
from simulation import Simulation
from copy import deepcopy

class Node():

    def __init__(self, game, ind, parent_ind, parent_move_x, parent_move_y):
        self.positions = [player.position for player in game.players]
        self.cards = [player.cards[:] for player in game.players]
        self.player = game.players[game.turn]
        self.is_terminal = game.is_over()

        self.wins = 0
        self.losses = 0
        self.visits = 0
        self.ind = ind
        self.parent_ind = parent_ind

        self.parent_move_x = 0
        self.parent_move_y = 0
        
        self.legal_moves = game.get_legal_moves(player=game.players[game.turn])
        self.num_of_legal_moves = sum(len(l) for l in self.legal_moves)
        self.children = []
        self.has_children = False
        self.next_move_x = 0 #Very non-elegant solution
        self.next_move_y = 0 ############### as a start

        self.nodes_expanded = 0
        self.all_expanded = False

class MCTS():

    def __init__(self, num_iters, gamestate):
        self.tree = [0] * (num_iters + 1)
        self.max_ind = 0
        self.game = deepcopy(gamestate)
        self.sim = Simulation()

    def UCB1(self, node):
        ret = []
        for ind in node.children:
            temp = self.tree[ind]
            if temp.visits == 0:
                ret.append(123456789) #inf
                continue
            
            if temp.player != 0:
                wr = 1 - temp.wins/temp.visits
            else:
                wr = temp.wins/temp.visits
            ret.append(wr + C_PARAMETER * (np.log(node.visits) / temp.visits) ) #UCB1 formula
        return ret

    def selection(self, node):
        while True:
            if not node.all_expanded:
                return node
            if node.has_children:
                selected_ind = np.argmax(self.UCB1(node))
                node = self.tree[node.children[selected_ind]]
                continue
            break
        return node

    def expansion(self, node):
        if node.is_terminal:
            return
        if not node.all_expanded:
            self.game.set_state(node.positions, node.cards)
            
            vehicle = node.next_move_x #coordinates in a jagged array
            position = node.legal_moves[node.next_move_x][node.next_move_y]
            
            self.game.make_move(node.player, vehicle, position)
            self.game.turn = (self.game.turn + 1) % len(self.game.players)

            self.max_ind += 1
            child = Node(self.game, self.max_ind, node.ind, node.next_move_x, node.next_move_y)
            self.tree[self.max_ind] = child
            node.children.append(child.ind)
            node.nodes_expanded += 1
            node.has_children = True
            if node.nodes_expanded == node.num_of_legal_moves:
                node.all_expanded = True

            node.next_move_y += 1 #Sets up indices for the next move
            while node.next_move_y >= len(node.legal_moves[node.next_move_x]):
                if (node.next_move_x >= 4):
                    break
                node.next_move_y = 0
                node.next_move_x += 1


    def simulation(self, node):
        self.sim.det_wins = 0
        self.sim.mrx_wins = 0
        self.game.set_state(node.positions, node.cards)
        
        self.sim.simulate_game(self.game)

        if self.sim.det_wins > 0:
            return 0
        if self.sim.mrx_wins > 0:
            return 1

    def backpropagation(self, node, result):
        node.visits += 1
        node.wins += result
        
        if node.ind == 0:
            return
        self.backpropagation(self.tree[node.parent_ind], result)

    def create_root_node(self):
        self.tree[0] = Node(self.game, 0, None, None, None)
        self.tree[0].visits = 1

    def search(self, num_iters):
        self.create_root_node()
        node = self.tree[0]
        for _ in range (num_iters):
            node = self.selection(self.tree[0])
            self.expansion(node)
            node = self.selection(node)
            result = self.simulation(node)
            self.backpropagation(node, result)
        node = self.tree[0]
        weights = [self.tree[x].visits for x in node.children]
        print("Weights:", weights)
        node = self.tree[node.children[np.argmax(weights)]]
        vehicle = node.parent_move_x
        position = self.tree[0].legal_moves[node.parent_move_x][node.parent_move_y]
        return [vehicle, position]
        

def main():
    board = Board("tax.txt", "bus.txt", "udg.txt", "rvr.txt")   
    d1 = Detective("Detective 1")
    d2 = Detective("Detective 2")
    mrx = MrX("Mr. X")
    detectives = [d1, d2]
    game = Game(detectives, mrx, board)
    game.turn = 0
    mcts = MCTS(100000, game)

    print(mcts.search(100000))
    print(mcts.tree[0].legal_moves)

    """#Creates root node
    mcts.create_root_node()
    print("Root legal moves:", mcts.tree[0].legal_moves)
    print("------------------------------------------")
    
    #Tests if expansion works
    for ind in range(sum(len(l) for l in mcts.tree[0].legal_moves)):
        print(mcts.tree[0].next_move_x, mcts.tree[0].next_move_y)
        mcts.expansion(mcts.tree[0])
        print("Nodes expanded:", mcts.tree[0].all_expanded)
        print("Max ind:", mcts.max_ind)
        print("Len of children:", len(mcts.tree[0].children))
        print(f"Child {ind} legal moves:", mcts.tree[mcts.max_ind].legal_moves)
        print("------------------------------------------")
        for _ in range(sum(len(l) for l in mcts.tree[ind].legal_moves)):
            mcts.expansion(mcts.tree[ind])
    print("Children of root node:", mcts.tree[0].children)
    print("Number of nodes:", mcts.max_ind)
    print("Parent of last node:", mcts.tree[mcts.max_ind].parent_ind)
    print("Legal moves of last node:", mcts.tree[mcts.max_ind].legal_moves)
    
    #Tests if selection works
    ind_leaf = mcts.tree[1].children[0]
    print("First leaf node:", ind_leaf)
    mcts.tree[ind_leaf].wins = 10
    mcts.tree[ind_leaf].visits = 20
    leaf = mcts.selection(mcts.tree[0]).ind
    print("Selected node:", leaf)
    print("UCB1 scores of first child of root", mcts.UCB1(mcts.tree[1]))
    print("Root wins, visits:", mcts.tree[0].wins, mcts.tree[0].visits)
    result = mcts.simulation(mcts.tree[leaf])
    print("Result of simulation:", result)
    mcts.backpropagation(mcts.tree[leaf], result)
    print("Root wins, visits:", mcts.tree[0].wins, mcts.tree[0].visits)"""

if __name__ == '__main__':
    main()
