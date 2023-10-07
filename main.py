import random
import os

# Function to check if a number is in the list of available coordinates
def check(num:int, coords:list) -> bool:
    """
    Function return True if num in coords
    False if not
    """
    return num in coords

# Function to draw the tic-tac-toe board
def draw_board(board:list) -> None:
    """
    Function draws tic tac toe board
    """
    os.system('cls')
    for i in range(len(board)):
        if i == 3 or i == 6:
            print()
        print(board[i], end='')
    print()

# Function to update the board after a move
def update_board(board:list, num:int, current_player:str, coords:list) -> None:
    """
    Function for update tic-tac-toe board 
    """
    player_marker = '|X|' if current_player == 'X' else '|O|'
    board[num - 1] = player_marker
    coords.remove(num)

# Function to make a random choice for the bot's move
def random_choice(coords:list) -> int:
    """
    Function returns random number from coords
    """
    return random.choice(coords)

# Function to check if there is a winner or a draw
def check_for_win(board:list, moves:int) -> str:
    """
    Function checks if there is a winner or a draw
    If moves is equal to 9 its draw
    """
    if (board[0] == board[1] == board[2] == '|X|') or \
       (board[3] == board[4] == board[5] == '|X|') or \
       (board[6] == board[7] == board[8] == '|X|') or \
       (board[0] == board[3] == board[6] == '|X|') or \
       (board[1] == board[4] == board[7] == '|X|') or \
       (board[2] == board[5] == board[8] == '|X|') or \
       (board[0] == board[4] == board[8] == '|X|') or \
       (board[6] == board[4] == board[2] == '|X|'):
        return 'X'
    elif (board[0] == board[1] == board[2] == '|O|') or \
         (board[3] == board[4] == board[5] == '|O|') or \
         (board[6] == board[7] == board[8] == '|O|') or \
         (board[0] == board[3] == board[6] == '|O|') or \
         (board[1] == board[4] == board[7] == '|O|') or \
         (board[2] == board[5] == board[8] == '|O|') or \
         (board[0] == board[4] == board[8] == '|O|') or \
         (board[6] == board[4] == board[2] == '|O|'):
        return 'O'
    else:
        if moves == 9:
            return 'draw'

# Main game loop
def main():
    print(f"{'-' * 20}Tic-Tac-Toe{'-' * 20}\nX or O 👇")

    bot_turn = False
    player_turn = False

    player_char = ''
    bot_char = ''

    moves = 0

    # Get user's choice of X or O
    choose = input('->: ').upper()
    if choose == 'X':
        player_turn = True
        player_char = 'X'
        bot_char = 'O'
    elif choose == 'O':
        bot_turn = True
        player_char = 'O'
        bot_char = 'X'
    else:
        print(f'Choose the right option x or y not {choose}')
        exit()

    # Initialize available coordinates and board
    coords = [i for i in range(1, 10)]
    board = ['|1|', '|2|', '|3|', '|4|', '|5|', '|6|', '|7|', '|8|', '|9|']

    while True:
        if bot_turn:
            # Bot's move
            if check(random_choice(coords), coords):
                update_board(board, random_choice(coords), bot_char, coords)
                print("Bot's move")
                draw_board(board)
            else:
                break
        else:
            try:
                # Player's turn
                chosen_number = int(input('Your turn: '))
                if check(chosen_number, coords):
                    update_board(board, chosen_number, player_char, coords)
                    draw_board(board)
                else:
                    print("Invalid choice. Please select a number between 1 and 9 that hasn't been chosen yet.")
                    break
            except ValueError:
                print('Please input only numbers')

        player_turn = not player_turn
        bot_turn = not bot_turn
        moves += 1

        winner = check_for_win(board, moves)
        if winner == player_char:
            print('You won')
            break
        elif winner == bot_char:
            print('Bot won')
            break
        elif winner == 'draw':
            print('Its a draw')
            break

if __name__ == '__main__':
    main()
