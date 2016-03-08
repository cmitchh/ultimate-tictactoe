#! /usr/bin/env python
import sys
import pdb

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
	print(" "+A[3]+" "+A[4]+" "+A[5]+"  |  "+B[3]+" "+B[4]+" "+B[5]+"  |  "+C[3]+" "+C[4]+" "+C[5])
	print(" "+A[6]+" "+A[7]+" "+A[8]+"  |  "+B[6]+" "+B[7]+" "+B[8]+"  |  "+C[6]+" "+C[7]+" "+C[8])
	print("________|_________|_______")
	print("        |         |        ")
	print(" "+D[0]+" "+D[1]+" "+D[2]+"  |  "+E[0]+" "+E[1]+" "+E[2]+"  |  "+F[0]+" "+F[1]+" "+F[2])
	print(" "+D[3]+" "+D[4]+" "+D[5]+"  |  "+E[3]+" "+E[4]+" "+E[5]+"  |  "+F[3]+" "+F[4]+" "+F[5])
	print(" "+D[6]+" "+D[7]+" "+D[8]+"  |  "+E[6]+" "+E[7]+" "+E[8]+"  |  "+F[6]+" "+F[7]+" "+F[8])
	print("________|_________|_______")
	print("        |         |        ")
	print(" "+G[0]+" "+G[1]+" "+G[2]+"  |  "+H[0]+" "+H[1]+" "+H[2]+"  |  "+I[0]+" "+I[1]+" "+I[2])
	print(" "+G[3]+" "+G[4]+" "+G[5]+"  |  "+H[3]+" "+H[4]+" "+H[5]+"  |  "+I[3]+" "+I[4]+" "+I[5])
	print(" "+G[6]+" "+G[7]+" "+G[8]+"  |  "+H[6]+" "+H[7]+" "+H[8]+"  |  "+I[6]+" "+I[7]+" "+I[8]+"\n")

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
		play(board, activeplayer, mark)

def updateboards(A, B, C, D, E, F, G, H, I, move, board, activeplayer, mark):
	if (board == "A"):
		validmark = checkspace(move, A, activeplayer, mark, board)
		A[move] = validvalidmark
	elif (board =="B"):
		validmark = checkspace(move, B, activeplayer, mark, board)
		B[move] = validmark
	elif (board =="C"):
		validmark = checkspace(move, C, activeplayer, mark, board)
		C[move] = validmark
	elif (board =="D"):
		validmark = checkspace(move, D, activeplayer, mark, board)
		D[move] = validmark
	elif (board =="E"):
		validmark = checkspace(move, E, activeplayer, mark, board)
		E[move] = validmark
	elif (board =="F"):
		validmark = checkspace(move, F, activeplayer, mark, board)
		F[move] = validmark
	elif (board =="G"):
		validmark = checkspace(move, G, activeplayer, mark, board)
		G[move] = validmark
	elif (board =="H"):
		validmark checkspace(move, H, activeplayer, mark, board)
		H[move] = validmark
	else:
		validmark = checkspace(move, I, activeplayer, mark, board)
		I[move] = validmark
	return A, B, C, D, E, F, G, H, I

#check to see if space is free
def checkspace(move, boardcontents, activeplayer, mark, board):
	while (boardcontents[move] == "x" or boardcontents[move] == "o"):
		print ("This square is taken")
		mark = raw_input("\nPlayer "+activeplayer+": Enter a free space on board "+board+" to place an "+mark+"\n>>")
	return mark
		



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

def checksmallboards(A, B, C, D, E, F, G, H, I, Overall, mark):
		#this needs simplifying
		if ((check(A) == True) and (A[9] == "open")):
			Overall[0] = mark
			if (mark == "x"):
				A = ["\\", " ", "/", " ", "X", " ", "/", " ", "\\", "won"]
			else:
				A = ["/", " ", "\\", "|", " ", "|", "\\", " ", "/", "won"]
			return A, B, C, D, E, F, G, H, I, Overall
		elif ((check(B) == True) and (B[9] == "open")):
			if (mark == "x"):
				B = ["\\", " ", "/", " ", "X", " ", "/", " ", "\\", "won"]
			else:
				B = ["/", " ", "\\", "|", " ", "|", "\\", " ", "/", "won"]
			Overall[1] = mark
			return A, B, C, D, E, F, G, H, I, Overall
		elif ((check(C) == True) and (C[9] == "open")):
			if (mark == "x"):
				C = ["\\", " ", "/", " ", "X", " ", "/", " ", "\\", "won"]
			else:
				C = ["/", " ", "\\", "|", " ", "|", "\\", " ", "/", "won"]
			Overall[2] = mark 
			return A, B, C, D, E, F, G, H, I, Overall
		elif ((check(D) == True) and (D[9] == "open")):
			if (mark == "x"):
				D = ["\\", " ", "/", " ", "X", " ", "/", " ", "\\", "won"]
			else:
				D = ["/", " ", "\\", "|", " ", "|", "\\", " ", "/", "won"]
			Overall[3] = mark
			return A, B, C, D, E, F, G, H, I, Overall
		elif ((check(E) == True) and (E[9] == "open")):
			if (mark == "x"):
				E = ["\\", " ", "/", " ", "X", " ", "/", " ", "\\", "won"]
			else:
				E = ["/", " ", "\\", "|", " ", "|", "\\", " ", "/", "won"]
			Overall[4] = mark
			return A, B, C, D, E, F, G, H, I, Overall
		elif ((check(F) == True) and (F[9] == "open")):
			if (mark == "x"):
				F = ["\\", " ", "/", " ", "X", " ", "/", " ", "\\", "won"]
			else:
				F = ["/", " ", "\\", "|", " ", "|", "\\", " ", "/", "won"]
			Overall[5] = mark
			return A, B, C, D, E, F, G, H, I, Overall
		elif ((check(G) == True) and (G[9] == "open")):
			if (mark == "x"):
				G = ["\\", " ", "/", " ", "X", " ", "/", " ", "\\", "won"]
			else:
				G = ["/", " ", "\\", "|", " ", "|", "\\", " ", "/", "won"]
			Overall[6] = mark
			return A, B, C, D, E, F, G, H, I, Overall
		elif ((check(H) == True) and (H[9] == "open")):
			if (mark == "x"):
				H = ["\\", " ", "/", " ", "X", " ", "/", " ", "\\", "won"]
			else:
				H = ["/", " ", "\\", "|", " ", "|", "\\", " ", "/", "won"]
			Overall[7] = mark
			return A, B, C, D, E, F, G, H, I, Overall
		elif ((check(I) == True) and (I[9] == "open")):
			if (mark == "x"):
				I = ["\\", " ", "/", " ", "X", " ", "/", " ", "\\", "won"]
			else:
				I = ["/", " ", "\\", "|", " ", "|", "\\", " ", "/", "won"]
			Overall[8] = mark
			return A, B, C, D, E, F, G, H, I, Overall
		else:
			return A, B, C, D, E, F, G, H, I, Overall

def checkoverallboard(Overall, activeplayer):
	state = check(Overall)
	activeplayer = str(activeplayer)
	if (state == True):
		print ("Game Over\nPlayer "+activeplayer+" wins!")
		return True
	else:
		return False


def check(board):
	if ((board[0] == board[1] == board[2]) or (board[0] == board[3] == board[6]) or (board[0] == board[4] == board[8]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]) or (board[2] == board[4] == board[6])):
		return True
	else:
		return False

def checkforcats(board):
	if((board[0] == "x" or board[0] == "y") and (board[1] == "x" or board[1] == "y") and (board[2] == "x" or board[2] == "y") and (board[3] == "x" or board[3] == "y") and (board[4] == "x" or board[4] == "y") and (board[5] == "x" or board[5] == "y") and (board[6] == "x" or board[6] == "y") and (board[7] == "x" or board[7] == "y") and (board[8] == "x" or board[8] == "y")):
		print True
		return True
	else:
		print False
		return False

def checksmallcats(A, B, C, D, E, F, G, H, I):
	if (checkforcats(A) == True and A[9] == "open"):
		A = [" ", "*", " ", "*", "*", "*", "*", " ", "*", "cats"]
		return A, B, C, D, E, F, G, H, I
	elif (checkforcats(B) == True and B[9] == "open"):
		B = [" ", "*", " ", "*", "*", "*", "*", " ", "*", "cats"]
		return A, B, C, D, E, F, G, H, I
	elif (checkforcats(C) == True and C[9] == "open"):
		C = [" ", "*", " ", "*", "*", "*", "*", " ", "*", "cats"]
		return A, B, C, D, E, F, G, H, I
	elif (checkforcats(D) == True and D[9] == "open"):
		D = [" ", "*", " ", "*", "*", "*", "*", " ", "*", "cats"]
		return A, B, C, D, E, F, G, H, I
	elif (checkforcats(E) == True and E[9] == "open"):
		E = [" ", "*", " ", "*", "*", "*", "*", " ", "*", "cats"]
		return A, B, C, D, E, F, G, H, I
	elif (checkforcats(F) == True and F[9] == "open"):
		F = [" ", "*", " ", "*", "*", "*", "*", " ", "*", "cats"]
		return A, B, C, D, E, F, G, H, I
	elif (checkforcats(G) == True and G[9] == "open"):
		G = [" ", "*", " ", "*", "*", "*", "*", " ", "*", "cats"]
		return A, B, C, D, E, F, G, H, I
	elif (checkforcats(H) == True and H[9] == "open"):
		H = [" ", "*", " ", "*", "*", "*", "*", " ", "*", "cats"]
		return A, B, C, D, E, F, G, H, I
	elif (checkforcats(I) == True and I[9] == "open"):
		I = [" ", "*", " ", "*", "*", "*", "*", " ", "*", "cats"]
		return A, B, C, D, E, F, G, H, I
	else:
		return A, B, C, D, E, F, G, H, I
		




 
def nextboard(A, B, C, D, E, F, G, H, I, lmove):
	board = lmove
	if ((board == "A") and (A[9] == "open")):
		return board
	elif ((board == "B") and (B[9] == "open")):
		return board
	elif ((board == "C") and (C[9] == "open")):
		return board
	elif ((board == "D") and (D[9] == "open")):
		return board
	elif ((board == "E") and (E[9] == "open")):
		return board
	elif ((board == "F") and (F[9] == "open")):
		return board
	elif ((board == "G") and (G[9] == "open")):
		return board
	elif ((board == "H") and (H[9] == "open")):
		return board
	elif ((board == "I") and (I[9] == "open")):
		return board
	else:
		nboard = getnewboard(A, B, C, D, E, F, G, H, I)
		return nboard

		
def getnewboard(A, B, C, D, E, F, G, H, I):
	board = raw_input("\nSelect an open board to play on, by entering a number from A to I \n>>")
	if ((board == "A" and A[9] == "open") or (board == "B" and B[9] == "open") or (board == "C" and C[9] == "open") or (board == "D" and D[9] == "open") or (board == "E" and E[9] == "open")or (board == "F" and F[9] == "open") or (board == "G" and G[9] == "open") or (board == "H" and H[9] == "open") or (board == "I" and I[9] == "open")):
		return board
	else:
		print ("\nThat is not a valid board selection\n")
		return getnewboard(A, B, C, D, E, F, G, H, I)






def main():
	welcome()
	#initialize and print boards
	A, B, C, D, E, F, G, H, I, Overall = createboards()
	displayboard(A, B, C, D, E, F, G, H, I, Overall)
	#player 1 selects starting board
	board = begin()	
	activeplayer = 1
	mark = "x"
	wincondition = False
	#play starts
	pdb.set_trace()
	while (wincondition == False):
		move, lmove = play(board, activeplayer, mark)
		A, B, C, D, E, F, G, H, I = updateboards(A, B, C, D, E, F, G, H, I, move, board, activeplayer, mark)
		A, B, C, D, E, F, G, H, I, Overall = checksmallboards(A, B, C, D, E, F, G, H, I, Overall, mark)
		A, B, C, D, E, F, G, H, I = checksmallcats(A, B, C, D, E, F, G, H, I)
		displayboard(A, B, C, D, E, F, G, H, I, Overall)
		wincondition = checkoverallboard(Overall, activeplayer)
		board = nextboard(A, B, C, D, E, F, G, H, I, lmove)
		activeplayer, mark = switchplayer(activeplayer)
	



#todo: 
#overall cats check
#fix small cats check
#fix square is taken error

#\   /
#  X
#/   \

#/   \
#|   |
#\   /







main()
