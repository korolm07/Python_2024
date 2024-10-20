print("Welcone to Tic Tac Toe game!\nImagine that the bord is a numpad:")
print ("789\n456\n123")
print ("So when asked to provide a number-posistion, simply put number corresponding to numpad. Good luck!")
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
current_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(current_board)
choice = input ("Player 1: Do you want to be X or O? ")
if choice == 'X':
    print ("Player 1: will go first")
elif choice == "O":
    print ("Player 2: will go first")

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

game_on = True
while game_on:
    wrong_position_x = True
    while wrong_position_x:
        position = int(input ("Choose your X position: (1-9) "))
        if position in range (1,10) and current_board [position] == ' ':
            current_board [position] = 'X'
            display_board(current_board)
            wrong_position_x = False
    if win_check(current_board,"X"):
        print ("Congratulations! X have won the game!")
        game_on = False
        break

    wrong_position_o = True
    while wrong_position_o:
        position = int(input ("Choose your O position: (1-9) "))
        if position in range (1,10) and current_board [position] == ' ':
            current_board [position] = 'O'
            display_board(current_board)
            wrong_position_o = False
    if win_check(current_board,'O'):
        print ("Congratulations! O have won the game!")
        game_on = False
        break
 
    

