board = [" " for x in range(9)]

def print_board():
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"
    print(row1)
    print(row2)
    print(row3)


def move(icon):
    while True:
     try:
        choice = int(input('Its your turn, enter your move (0-8)'))
     except ValueError:
        print("Please enter a number (0-8)")
        continue
     if board[choice] == ' ':
        board[choice] = icon
        break
     else:
        print('That space is taken')
        
        
def victory(icon):
     if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
     else:
        return False

    
def game():
   while True:
    print_board()
    move("X")
    print_board()
    if victory("X"):
        print("X wins! Congratulations!")
        break
    elif " " not in board:
        print("You have a draw!")
        break
    move("O")
    if victory("O"):
        print_board()
        print("O wins! Congratulations!")
        break
    elif " " not in board:
        print("You have a draw")
        break

game()




    
        
        



    

