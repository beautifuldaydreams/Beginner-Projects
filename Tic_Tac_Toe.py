board = [" ", " "," "," "," "," "," "," "," "]
i = 0
a = 0

def display_board():
	print(board[0] + "|" + board[1] + "|" + board[2])
	print("-----")
	print(board[3] + "|" + board[4] + "|" + board[5])
	print("-----")
	print(board[6] + "|" + board[7] + "|" + board[8])

def user_input():
	global i
	if i == 0:
		board[position - 1] = "X"
		i += 1
		display_board()
	else:
		board[position -1] = "O"
		i -= 1
		display_board()
	return i

def check_board_full():
	if board[position -1] != " ":
		return True

def check_winner():
	global a
	if (board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5] == "X") or (board[6] == board[7] == board[8] == "X")\
		or (board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X")\
		or (board[0] == board[4] == board[8] == "X") or (board[2] == board[4] == board[6] == "X"):
		a = 1
		return a
	if (board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5] == "O") or (board[6] == board[7] == board[8] == "O")\
		or (board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7] == "O") or (board[2] == board[5] == board[8] == "O")\
		or (board[0] == board[4] == board[8] == "O") or (board[2] == board[4] == board[6] == "O"):
		a = 2
		return a

if __name__ == "__main__":
	print("Welcome to Tic Tac Toe.")
	display_board()
	i = 0
	while True:
		try:
			if i == 0:
				position = int(input("Please enter a position 1-9:\n"))
				if check_board_full():
					print("Please chose an empty space.")
				else:
					user_input()
				check_winner()
				if a == 1:
					print("Player One wins!")
				elif a == 2:
					print("Player Two wins!")
			elif i == 1:
				position = int(input("Please enter a position 1-9:"))
				if check_board_full():
					print("Please chose an empty space.")
				else:
					user_input()
				check_winner()
				if a == 1:
					print("Player One wins!")
					break
				elif a == 2:
					print("Player Two wins!")
					break
		except ValueError:
			print("Please enter a valid number.")
