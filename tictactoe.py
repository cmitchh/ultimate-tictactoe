#! /usr/bin/env python
import sys

def welcome():
	print("\nWelcome to Ultimate Tic-Tac-Toe!\n")
	print("Rules: The goal is to create a line of three won boards.\nA board is won when a line of X's or O's is created. \nLike in the simple version, players alternate turns\nplacing their symbol in a square by entering a letter\nA-I indicating their selected square. The catch is that\nwhichever square a player places their symbol is then\nthe square on the overall board that the opponent must\nplay in. If a player is sent to a completed square, they \nget to choose which board to play on.\n")
	print("\nPlayer 1 is x\nPlayer 2 is o\n")

def createboards():
	#indices 0-8 are board spaces, index 9 is board state (won or not)
	A = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "open"]
	B = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "open"]
	C = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "open"]
	D = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "open"]
	E = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "open"]
	F = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "open"]
	G = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "open"]
	H = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "open"]
	I = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "open"]
	Overall = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
	return A, B, C, D, E, F, G, H, I, Overall

def displayboard(A, B, C, D, E, F, G, H, I, Overall):
	print("\n "+A[0]+" "+A[1]+" "+A[2]+"  |  "+B[0]+" "+B[1]+" "+B[2]+"  |  "+C[0]+" "+C[1]+" "+C[2])
	print(" "+A[3]+" "+A[4]+" "+A[5]+"  |  "+B[3]+" "+B[5]+" "+B[5]+"  |  "+C[3]+" "+C[4]+" "+C[5])
	print(" "+A[5]+" "+A[7]+" "+A[8]+"  |  "+B[6]+" "+B[7]+" "+B[8]+"  |  "+C[6]+" "+C[7]+" "+C[8])
	print("________|_________|_______")
	print("        |         |        ")
	print(" "+D[0]+" "+D[1]+" "+D[2]+"  |  "+E[0]+" "+E[1]+" "+E[2]+"  |  "+F[0]+" "+F[1]+" "+F[2])
	print(" "+D[3]+" "+D[4]+" "+D[5]+"  |  "+E[3]+" "+E[5]+" "+E[5]+"  |  "+F[3]+" "+F[4]+" "+F[5])
	print(" "+D[5]+" "+D[7]+" "+D[8]+"  |  "+E[6]+" "+E[7]+" "+E[8]+"  |  "+F[6]+" "+F[7]+" "+F[8])
	print("________|_________|_______")
	print("        |         |        ")
	print(" "+G[0]+" "+G[1]+" "+G[2]+"  |  "+H[0]+" "+H[1]+" "+H[2]+"  |  "+I[0]+" "+I[1]+" "+I[2])
	print(" "+G[3]+" "+G[4]+" "+G[5]+"  |  "+H[3]+" "+H[5]+" "+H[5]+"  |  "+I[3]+" "+I[4]+" "+I[5])
	print(" "+G[5]+" "+G[7]+" "+G[8]+"  |  "+H[6]+" "+H[7]+" "+H[8]+"  |  "+I[6]+" "+I[7]+" "+I[8]+"\n")

def begin():
	board = raw_input("\nPlayer 1: Select a board to begin with, by entering a number from A to I \n>>")
	if (board == "A" or board == "B" or board == "C" or board == "D" or board == "E" or board == "F" or board == "G" or board == "H" or board == "I"):
		return board
	else:
		print ("\nThat is not a valid board selection\n")
		begin()
 
def play(board, activeplayer, mark):
	activeplayer = str(activeplayer)
	lmove = raw_input("\nPlayer "+activeplayer+": Enter a space on board "+board+" to place an "+mark+"\n>>")
	if (lmove == "A" or lmove == "B" or lmove == "C" or lmove == "D" or lmove == "E" or lmove == "F" or lmove == "G" or lmove == "H" or lmove == "I"):
		move = ltoint(lmove)
		return move, lmove
	else:
		print ("\nThat is not a valid square\n")
		play()

def updateboards(A, B, C, D, E, F, G, H, I, move, board, activeplayer, mark):
	if (board == "A"):
		checkspace(move, A)
		A[move] = mark
	elif (board =="B"):
		checkspace(move, B)
		B[move] = mark
	elif (board =="C"):
		checkspace(move, C)
		C[move] = mark
	elif (board =="D"):
		checkspace(move, D)
		D[move] = mark
	elif (board =="E"):
		checkspace(move, E)
		E[move] = mark
	elif (board =="F"):
		checkspace(move, F)
		F[move] = mark
	elif (board =="G"):
		checkspace(move, G)
		G[move] = mark
	elif (board =="H"):
		checkspace(move, H)
		H[move] = mark
	else:
		checkspace(move, I)
		I[move] = mark
	return A, B, C, D, E, F, G, H, I

#check to see if space is free
def checkspace(move, board):
	while (board[move] == "x"):
		print ("This square is taken")
		play()
	while (board[move] == "o"):
		print ("This square is taken")
		play()


#takes inputted letter and changes it into an integer to simplify computation
def ltoint(letter):
	if (letter == "A"):
		return 0
	elif (letter == "B"):
		return 1
	elif (letter == "C"):
		return 2
	elif (letter == "D"):
		return 3
	elif (letter == "E"):
		return 4
	elif (letter == "F"):
		return 5
	elif (letter == "G"):
		return 6
	elif (letter == "H"):
		return 7
	elif (letter == "I"):
		return 8
	else:
		print("invalid letter value")
		return letter


def switchplayer(activeplayer):
	if activeplayer == 1:
		activeplayer = 2
		mark = "o"

	else:
		activeplayer = 1
		mark = "x"
	return activeplayer, mark

#def checksmallboards(A, B, C, D, E, F, G, H, I):
#	if ( )






def main():
	welcome()
	A, B, C, D, E, F, G, H, I, Overall = createboards()
	displayboard(A, B, C, D, E, F, G, H, I, Overall)
	board = begin()	
	activeplayer = 1
	mark = "x"
	wincondition = False

	while (wincondition == False):
		move, lmove = play(board, activeplayer, mark)
		A, B, C, D, E, F, G, H, I = updateboards(A, B, C, D, E, F, G, H, I, move, board, activeplayer, mark)
		displayboard(A, B, C, D, E, F, G, H, I, Overall)
		#checksmallboards(A, B, C, D, E, F, G, H, I)
		board = lmove
		activeplayer, mark = switchplayer(activeplayer)
	
	print("Player %d wins!" % activeplayer)


#todo: 
#check to see if move wins a board, 
#if move wins update overall board (check if overall board is won), 
#check if next board is complete

#figure out why P2 first turn doesnt register





main()
