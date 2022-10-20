def horizontal_line ( size ):
    return " ---" * size + " \n"

def vertical_lines ( size ):
    return "|   " * size + "|\n"

def gameboard ( size ):
    board = """"""
    for i in range(size):
        board += horizontal_line(size)
        board += vertical_lines(size)
    board += horizontal_line(size)
    return board

def printBoard():
    print(gameboard(20))