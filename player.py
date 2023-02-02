from random import shuffle

starting_positions = [1, 2, 3, 4, 5]

## broj kartica je isto trentuno harcodean al to se moze promijeniti
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
DETECTIVE_TAX = 10
DETECTIVE_BUS = 8
DETECTIVE_UDG = 4
MRX_TAX = 4
MRX_BUS = 3
MRX_UDG = 2
MRX_INVISIBLE = 5
MRX_X2 = 2

class Player():
	def __init__(self, name=""):
		self.name = name
		shuffle(starting_positions)
		self.positions = [starting_positions.pop()]
		self.tax_cards = 0
		self.bus_cards = 0
		self.udg_cards = 0
		self.invisible_cards = 0
		self.x2_cards = 0

## jel potrebno imat posebne klase za detektive i mr x
## tj. jel mr x treba neke posebne metode/atribute
## myb stavit brojeve kartica kao argumente u init od Playera
## ???????????????????????????????????????????????????

class Detective(Player):
	def __init__(self, name=""):
		super(Detective, self).__init__(name)
		self.tax_cards = DETECTIVE_TAX
		self.bus_cards = DETECTIVE_BUS
		self.udg_cards = DETECTIVE_UDG


class MrX(Player):
	def __init__(self, name=""):
		super(MrX, self).__init__(name)
		self.tax_cards = MRX_TAX
		self.bus_cards = MRX_BUS
		self.udg_cards = MRX_UDG
		self.invisible_cards = MRX_INVISIBLE
		self.x2_cards = MRX_X2


def main():
	d1 = Player()
	mrx = MrX()
	print(d1.positions[0], mrx.positions[0], starting_positions)


if __name__ == '__main__':
	main()