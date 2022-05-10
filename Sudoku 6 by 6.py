sudoku = [[0, 0, 3, 0, 1, 0],
          [5, 6, 0, 3, 2, 0],
          [0, 5, 4, 2, 0, 3],
          [2, 0, 6, 4, 5, 0],
          [0, 1, 2, 0, 4, 5],
          [0, 4, 0, 1, 0, 0]]

def possible(row, column, number):
    global sudoku
    for i in range(0, 6):
        if sudoku[row][i] == number:
            return False

    for i in range(0, 6):
        if sudoku[i][column] == number:
            return False

    x0 = (column // 3)*3
    y0 = (row // 2)*2
    for i in range(0, 2):
        for j in range(0, 3):
            if sudoku[y0 + i][x0 + j] == number:
                return False

    return True


def solve():
    global sudoku
    for row in range(0, 6):
        for column in range(0, 6):
            if sudoku[row][column] == 0:
                for number in range(1, 7):
                    if possible(row, column, number):
                        sudoku[row][column] = number
                        solve()
                        

                        return

solve()
print(sudoku)


