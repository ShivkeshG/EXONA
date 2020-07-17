board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

game_still_going = True

winner = None

current_player = "X"

def play_game():
    display_board()



def display_board():
    print("\n")
print(board[0] + "|" + board[1] + "|" + board[2]) 
print(board[3] + "|" + board[4] + "|" + board[5]) 
print(board[6] + "|" + board[7] + "|" + board[8])
