class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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

    posi = Coordinate(int(coordinates[0]), int(coordinates[1]))

    size = len(brd)
    if posi.x >= size or posi.x < 0 or posi.y >= size or posi.y < 0:
        print('HIBA: ilyen pozíció nincs')
        return get_input(brd, nxt)
    if brd[posi.x][posi.y] != '#':
        print('HIBA: a mező már meg lett jelölve')
        return get_input(brd, nxt)
    return posi


if __name__ == '__main__':
    board_size = 4
    board = load_board(board_size)
    print_board(board)

    end_of_game = False
    next_player = 'X'
    while not end_of_game:
        position = get_input(board, next_player)
        board[position.x][position.y] = next_player
        print_board(board)
        next_player = 'O'
