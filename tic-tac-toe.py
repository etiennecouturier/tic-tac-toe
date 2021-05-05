class Coordinate:
    def __init__(self, row, column):
        self.x = row
        self.y = column


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


def get_input(brd, nxt):
    coordinates = input("{} következik>".format(nxt)).split(' ')
    if len(coordinates) != 2 or not coordinates[0].isdigit() or not coordinates[1].isdigit():
        print('HIBA: érvénytelen bemenet')
        return get_input(brd, nxt)

    row = int(coordinates[0])
    column = int(coordinates[1])

    size = len(brd)
    if row >= size or row < 0 or column >= size or column < 0:
        print('HIBA: ilyen pozíció nincs')
        return get_input(brd, nxt)
    if brd[row][column] != '#':
        print('HIBA: a mező már meg lett jelölve')
        return get_input(brd, nxt)
    return Coordinate(row, column)


def transpose(b):
    return [[b[j][i] for j in range(len(b))] for i in range(len(b[0]))]


def diagonal(b):
    return [b[i][i] for i in range(len(b))]


def any_row_completed(b, player):
    return any(all(elem == player for elem in row) for row in b)


def ended(b, player):
    return any_row_completed(b, player) \
           or any_row_completed(transpose(b), player) \
           or any_row_completed([diagonal(b)], player)


if __name__ == '__main__':
    board_size = 4
    board = load_board(board_size)
    print_board(board)

    next_player = 'X'
    while not ended(board, next_player):
        position = get_input(board, next_player)
        board[position.x][position.y] = next_player
        print_board(board)
        next_player = 'O'
