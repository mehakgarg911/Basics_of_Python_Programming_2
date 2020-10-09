def board():
	matrix = []
	for i in range(3): 
		matrix.append([])
	
	for i in range(3):
		for j in range(3):
			matrix[i].append(0)

def tictactoe():

	print("Welcome to the game! TIC TAC TOE")

	s=""
	print(type(s))

	while(s!=("X" or "O")):
		s= input("Please choose your side: X OR O :")

	print()

	for i in range(3):
		print(matrix[i])

	v = input("Please choose a position to place {} from 0 to 8: ".format(s))



		


tictactoe()