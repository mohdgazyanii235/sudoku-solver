import csv


# converts csv to matrix.
def csv_to_matrix(file_name):
    challenge = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            challenge.append(row)
            for j, value in enumerate(row):
                if value == '':
                    challenge[i][j] = 0
    return challenge


# Checks if that specific value is unique in the box.
def box_validator(challenge, x, y, value):
    value = str(value)
    if x == 1 or x == 4 or x == 7:
        x = x - 1
    elif x == 2 or x == 5 or x == 8:
        x = x - 2

    if y == 1 or y == 4 or y == 7:
        y = y - 1
    elif y == 2 or y == 5 or y == 8:
        y = y - 2

    end_x = x + 3
    end_y = y + 3
    while x < end_x:
        while y < end_y:
            if challenge[x][y] == value:
                return False
            y += 1
        y = y - 3
        x += 1
    return True


# Checks if that specific value is unique in that column
def vertical_validator(challenge, x, y, value):
    value = str(value)
    seen = 0
    # value = matrix[x][y]
    x = 0
    while x < 9:
        if challenge[x][y] == value:
            seen += 1
        x += 1
    if seen >= 1:
        return False
    return True


# Checks if that specific value is unique in that row
def horizontal_validator(challenge, x, y, value):
    value = str(value)
    # value = matrix[x][y]
    seen = 0
    y = 0
    while y < 9:
        if challenge[x][y] == value:
            seen += 1
        y += 1
    if seen >= 1:
        return False
    return True


def all_checks(challenge, x, y, value):
    if box_validator(challenge, x, y, value) and vertical_validator(challenge, x, y, value) and horizontal_validator(challenge, x, y, value):
        return True
    return False


def find_empty_cell(challenge):
    for x, row in enumerate(challenge):
        for y, value in enumerate(row):
            if value == 0:
                return x, y
    return None


def sudoku_solver(challenge):
    empty_cell = find_empty_cell(challenge)
    if not empty_cell:
        return True
    else:
        x, y = empty_cell

    i = 1
    while i < 10:
        if all_checks(challenge, x, y, i):
            challenge[x][y] = str(i)
            if sudoku_solver(challenge):
                return True

            challenge[x][y] = 0
        i += 1
    return False


def matrix_printer(challenge):
    for x in range(len(challenge)):
        for y in range(len(challenge[0])):
            if y < 8:
                print(str(challenge[x][y]) + " ", end='')
                if y % 3 == 2:
                    print("| ", end='')

            else:
                print(str(challenge[x][y]))
                if x % 3 == 2:
                    print("- - - - - - - - - - -  ")


board = csv_to_matrix('challenge1.csv')

print("printing challenge question: \n")
matrix_printer(board)
sudoku_solver(board)
print("\n\nPrinting solution: \n")
matrix_printer(board)

print(all_checks(board, 0, 2, 1))
