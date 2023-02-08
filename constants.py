MAX_STATION = 199

DETECTIVE_CARDS = [10, 8, 4, 0]
MRX_CARDS = [4, 3, 2, 5]

MAX_ROUNDS = 20

STARTING_POSITIONS = [103, 112, 34, 155, 94, 117, 132, 53, 174, 198, 50, 91, 26, 29, 141, 13, 138, 197]
TAKEN_POSITIONS = {position : 0 for position in STARTING_POSITIONS} #Makes sure two players can't start on the same spot

C_PARAMETER = 1.41421356

vehicle_to_idx = {"TAX": 0, "BUS": 1, "UDG": 2, "RVR": 3, "X2": 4}
idx_to_vehicle = {0: "TAX", 1: "BUS", 2: "UDG", 3: "RVR", 4: "X2"}
