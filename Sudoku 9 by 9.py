sudoku = [[0, 1, 5, 0, 0, 2, 8, 0, 9],
          [0, 0, 0, 0, 0, 1, 6, 0, 7],
          [0, 7, 0, 0, 0, 8, 4, 0, 0],
          [0, 0, 6, 0, 1, 7, 0, 4, 5],
          [0, 5, 3, 0, 0, 4, 7, 0, 0],
          [8, 4, 0, 0, 9, 5, 0, 6, 2],
          [0, 0, 4, 1, 7, 0, 0, 8, 6],
          [7, 6, 0, 5, 2, 0, 9, 1, 0],
          [5, 9, 1, 0, 8, 6, 0, 0, 0]]


def possible(row, column, number):
    global sudoku
    # Is the number appearing in the given row?
    for i in range(0, 9):
        if sudoku[row][i] == number:
            return False

    # Is the number appearing in the given column?
    for i in range(0, 9):
        if sudoku[i][column] == number:
            return False

    # Is the number appearing in the given square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0 + i][x0 + j] == number:
                return False

    return True


def solve():
    global sudoku
    for row in range(0, 9):
        for column in range(0, 9):
            if sudoku[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        sudoku[row][column] = number
                        solve()
                        sudoku[row][column] = 0

                return

    print(sudoku)
    input('More possible solutions')


solve()