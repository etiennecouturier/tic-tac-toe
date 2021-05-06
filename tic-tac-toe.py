import argparse


def get_arg():
    my_parser = argparse.ArgumentParser(description='tic-tac-toe game')
    my_parser.add_argument('board_size',
                           metavar='size of the board',
                           type=int,
                           help='board size')
    return my_parser.parse_args().board_size


def load_board(size):
    bord = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append('#')
        bord.append(row)
    return bord


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end='')
        print()


def get_input(board, nxt):
    coordinates = input("{} következik>".format(nxt)).split(' ')
    if len(coordinates) != 2 or not coordinates[0].isdigit() or not coordinates[1].isdigit():
        print('HIBA: érvénytelen bemenet')
        return get_input(board, nxt)

    row = int(coordinates[0])
    column = int(coordinates[1])

    size = len(board)
    if row >= size or row < 0 or column >= size or column < 0:
        print('HIBA: ilyen pozíció nincs')
        return get_input(board, nxt)
    if board[row][column] != '#':
        print('HIBA: a mező már meg lett jelölve')
        return get_input(board, nxt)
    return row, column


def next_player(curr_player):
    if curr_player == 'X':
        return 'O'
    return 'X'


def transpose(board):
    return [[board[column][row] for column in range(len(board))] for row in range(len(board[0]))]


def diagonal(board):
    return [board[i][i] for i in range(len(board))]


def any_row_completed(board, player):
    return any(all(elem == player for elem in row) for row in board)


def player_wins(board, player):
    if any_row_completed(board, player) \
            or any_row_completed(transpose(board), player) \
            or any_row_completed([diagonal(board)], player):
        print('Az {} játékos győzött!'.format(player))
        return True
    return False


def game_drawn(b):
    if not any(any(elem == '#' for elem in r) for r in b):
        print('Döntetlen!')
        return True
    return False


if __name__ == '__main__':
    game_board = load_board(get_arg())
    print_board(game_board)

    current_player = 'O'
    while not player_wins(game_board, current_player) and not game_drawn(game_board):
        current_player = next_player(current_player)
        board_row, col = get_input(game_board, current_player)
        game_board[board_row][col] = current_player
        print_board(game_board)
