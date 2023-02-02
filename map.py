class Map():
	def __init__(self, tax_filename="", bus_filename="", udg_filename=""):
		self.tax = read_map(tax_filename)
		self.bus = read_map(bus_filename)
		self.udg = read_map(udg_filename)	


def read_map(filename):
	## A dictionary is 6.6 times faster than a list when we lookup in 100 items.
	## https://towardsdatascience.com/faster-lookups-in-python-1d7503e9cd38

	## za sad cemo hardocodeat al kasnije promijenit myb
	## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	max_num = 199 + 1
	map = {index: [] for index in range(1, max_num)}
	
	with open(filename, 'r') as f:
		for line in f:
			line = line.rstrip()
			[start, end] = line.split()
			start = int(start)
			end = int(end)
			map[start].append(end)
		# print(map)
	
	return map


def main():
	""" tax_filename = input("Enter taxi filename: ")
	bus_filename = input("Enter bus filename: ")
	udg_filename = input("Enter underground filename: ") """
	tax_filename = "tax.txt"
	bus_filename = "bus.txt"
	udg_filename = "udg.txt"
	map = Map(tax_filename, bus_filename, udg_filename)

if __name__ == '__main__':
	main()