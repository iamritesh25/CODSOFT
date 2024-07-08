import math

board = [" " for _ in range(9)]

def print_board():
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def empty_squares():
    return " " in board

def make_move(square, letter):
    if board[square] == " ":
        board[square] = letter
        return True
    return False

def winner(b, l):
    win_conditions = [
        [b[0], b[1], b[2]],
        [b[3], b[4], b[5]],
        [b[6], b[7], b[8]],
        [b[0], b[3], b[6]],
        [b[1], b[4], b[7]],
        [b[2], b[5], b[8]],
        [b[0], b[4], b[8]],
        [b[2], b[4], b[6]],
    ]
    return [l, l, l] in win_conditions

def minimax(new_board, depth, is_maximizing):
    human = 'O'
    ai = 'X'

    if winner(new_board, human):
        return {'position': None, 'score': -1 * (len(available_moves()) + 1)}
    elif winner(new_board, ai):
        return {'position': None, 'score': 1 * (len(available_moves()) + 1)}
    elif not empty_squares():
        return {'position': None, 'score': 0}

    if is_maximizing:
        best = {'position': None, 'score': -math.inf}
        for possible_move in available_moves():
            new_board[possible_move] = ai
            sim_score = minimax(new_board, depth + 1, False)
            new_board[possible_move] = " "
            sim_score['position'] = possible_move
            if sim_score['score'] > best['score']:
                best = sim_score
        return best
    else:
        best = {'position': None, 'score': math.inf}
        for possible_move in available_moves():
            new_board[possible_move] = human
            sim_score = minimax(new_board, depth + 1, True)
            new_board[possible_move] = " "
            sim_score['position'] = possible_move
            if sim_score['score'] < best['score']:
                best = sim_score
        return best

def get_ai_move():
    if len(available_moves()) == 9:
        return 4
    else:
        return minimax(board, 0, True)['position']

def main():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while empty_squares():
        human_move = int(input("Choose a move (0-8): "))
        if human_move not in available_moves():
            print("Invalid move, try again.")
            continue

        make_move(human_move, 'O')
        print_board()

        if winner(board, 'O'):
            print("You win!")
            return
        elif not empty_squares():
            print("It's a tie!")
            return

        print("AI is making a move...")
        ai_move = get_ai_move()
        make_move(ai_move, 'X')
        print_board()

        if winner(board, 'X'):
            print("AI wins!")
            return
        elif not empty_squares():
            print("It's a tie!")
            return

if __name__ == '__main__':
    main()
