import random
import os

def check(num, coords):
    return num in coords

def draw_board(board):
    os.system('cls')
    for i in range(len(board)):
        if i == 3 or i == 6:
            print()
        print(board[i], end='')
    print()

def update_board(board, num, current_player='O', coords = []):
    player_marker = '|X|' if current_player == 'X' else '|O|'
    board[num - 1] = player_marker
    coords.remove(num)

def random_choice(coords):
    return random.choice(coords)

def check_for_win(board, moves):
    if (board[0] == board[1] == board[2] == '|X|') or (board[3] == board[4] == board[5] == '|X|') or (board[6] == board[7] == board[8] == '|X|') or (board[0] == board[3] == board[6] == '|X|') or (board[1] == board[4] == board[7] == '|X|') or (board[2] == board[5] == board[8] == '|X|') or (board[0] == board[4] == board[8] == '|X|') or (board[6] == board[4] == board[2] == '|X|'):
        return 'X'
    elif (board[0] == board[1] == board[2] == '|O|') or (board[3] == board[4] == board[5] == '|O|') or (board[6] == board[7] == board[8] == '|O|') or (board[0] == board[3] == board[6] == '|O|') or (board[1] == board[4] == board[7] == '|O|') or (board[2] == board[5] == board[8] == '|O|') or (board[0] == board[4] == board[8] == '|O|') or (board[6] == board[4] == board[2] == '|O|'):
        return 'O'
    else:
        if moves == 9:
            return 'Draw'
        else:
            return False

def main():
    print(f"{'-' * 20}Tic-Tac-Toe{'-' * 20}\nX or O 👇")

    bot_turn = False
    player_turn = False

    player_char = ''
    bot_char = ''

    moves = 0

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

    coords = [i for i in range(1, 10)]
    board = ['|1|', '|2|', '|3|', '|4|', '|5|', '|6|', '|7|', '|8|', '|9|']

    while True:
        if bot_turn:
            if check(random_choice(coords), coords):
                update_board(board, random_choice(coords), bot_char, coords)
                print("Bot's move")
                draw_board(board)
            else:
                break
        else:
            cord_choose = int(input('Your turn: '))
            if check(cord_choose, coords):
                update_board(board, cord_choose, player_char, coords)
                draw_board(board)
            else:
                break

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
        elif winner == 'Draw':
            print('Draw')
            break

if __name__ == '__main__':
    main()
