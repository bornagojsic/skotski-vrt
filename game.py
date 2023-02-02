from board import Board
from player import Detective, MrX

## dodat stvari ili maknut tu klasu
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Game():
	def __init__(self):
		pass


def get_possible_moves(player, board):
	tax = []
	bus = []
	udg = []
	rvr = []
	x2 = []
	
	if (player.tax_cards):
		tax = board.tax[player.positions[-1]]
	if (player.bus_cards):
		bus = board.bus[player.positions[-1]]
	if (player.udg_cards):
		udg = board.udg[player.positions[-1]]
	if (player.invisible_cards):
		rvr = board.rvr[player.positions[-1]] + tax + bus + udg
		## micanje duplikata
		rvr = list(set(rvr))
	if (player.x2_cards):
		## treba implementirat
		## !!!!!!!!!!!!!!!!!!!
		x1 = tax + bus + udg + rvr
		x2 = []
	moves = [tax, bus, udg, rvr, x2]
	return moves	


def make_move(player, mode, position, board):
	## limitirat kretanje mrxa na polja na kojima su detektivi
	## i detektiva isto lol
	## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	
	## dodaj mrxu karte koje su iskoristene
	## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	moves = get_possible_moves(player, board)
	if (mode == "TAX"):
		if position in moves[0]:
			player.positions.append(position)
			if isinstance(player, Detective):
				player.tax_cards -= 1
		else:
			raise Exception(f"{mode} {position} is not a legal move!")
	if (mode == "BUS"):
		if position in moves[1]:
			player.positions.append(position)
			if isinstance(player, Detective):
				player.bus_cards -= 1
		else:
			raise Exception(f"{mode} {position} is not a legal move!")
	if (mode == "UDG"):
		if position in moves[2]:
			player.positions.append(position)
			if isinstance(player, Detective):
				player.udg_cards -= 1
		else:
			raise Exception(f"{mode} {position} is not a legal move!")
	if (mode == "RVR"):
		if position in moves[3]:
			player.positions.append(position)
		else:
			raise Exception(f"{mode} {position} is not a legal move!")
	if (mode == "X2"):
		pass


def is_over(detectives, mrx):
	for detective in detectives:
		if detective.positions[-1] == mrx.positions[-1]:
			return True
	return False


def main():
	board = Board("tax.txt", "bus.txt", "udg.txt", "rvr.txt")

	d1 = Detective("Detecitve 1")
	d2 = Detective("Detective 2")
	mrx = MrX("Mr. X")
	for player in [d1, d2, mrx]:
		print(f"{player.name} position: {player.positions[-1]}")

	game = Game()

	while not is_over([d1, d2], mrx):
		print("Moves: [TAX, BUS, UDG, RVR, X2]")
		for player in [mrx, d1, d2]:
			print(f"{player.name} possible moves: {get_possible_moves(player, board)}")
		
		for player in [mrx, d1, d2]:
			## nacin inputa -> "vrsta transportacije" "nova pozicija"
			## npr: TAX 1
			player_move = input(f"{player.name} move: ")
			[mode, position] = player_move.split()
			position = int(position)
			make_move(player, mode, position, board)
	print("GAME OVER")
	exit()


if __name__ == "__main__":
	main()