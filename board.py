class Board():
	def __init__(self, tax_filename="", bus_filename="", udg_filename="", rvr_filename=""):
		self.tax = read_board(tax_filename)
		self.bus = read_board(bus_filename)
		self.udg = read_board(udg_filename)
		## rvr kao river
		self.rvr = read_board(rvr_filename)

## myb stavit u klasu ak nam kasnije nece trebat
## ?????????????????????????????????????????????
def read_board(filename):
	## A dictionary is 6.6 times faster than a list when we lookup in 100 items.
	## https://towardsdatascience.com/faster-lookups-in-python-1d7503e9cd38

	## za sad cemo hardcodeat al kasnije promijenit myb
	## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!???
	max_num = 199 + 1
	board = {index: [] for index in range(1, max_num)}
	
	with open(filename, 'r') as f:
		for line in f:
			line = line.rstrip()
			# print(line)
			# print(list(map(int, line.split())))
			[start, end] = list(map(int, line.split()))
			board[start].append(end)
			board[end].append(start)
		# print(board)
	
	return board


def main():
	""" tax_filename = input("Enter taxi filename: ")
	bus_filename = input("Enter bus filename: ")
	udg_filename = input("Enter underground filename: ") """
	tax_filename = "tax.txt"
	bus_filename = "bus.txt"
	udg_filename = "udg.txt"
	rvr_filename = "rvr.txt"
	board = Board(tax_filename, bus_filename, udg_filename)

if __name__ == '__main__':
	main()