#######################################
#                                     #
#  Script created by Mark L. Jensen   #
#  marklustyjensen@gmail.com          #
#  www.marklustyjensen.com            #
#                                     #
#######################################

# This function checkes to see if the chosen number is a valid or not.
def valid_num(board, row, col, num):
    # Checking the row for the same number.
    for i in range(9):
        if board[row][i] == num:
            return False
        
    # Checking the column for the same number.
    for i in range(9):
        if board[i][col] == num:
            return False
        
    # Finding the the 3x3 square in witch the number belongs.
    square_col = col - col % 3
    square_row = row - row % 3

    # Now checking if the square for the same number.
    for i in range(3):
        for j in range(3):
            if board[square_row + i][square_col + j] == num:
                return False
            
    # If all these check passes then the number is valid.
    return True

# This function will search for a solution to the sudoku, and return it when found.
def solve(board, row, col):
    # Checking to see if we have reached the end, and all fields have been assigned a value between 1 and 9.
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if board[row][col] > 0:
        return solve(board, row, col + 1)
    
    for num in range(1, 10):
        if valid_num(board, row, col, num):
            board[row][col] = num
            if solve(board, row, col + 1):
                return True
        board[row][col] = 0

    return False

def run_solve():
    if solve(board, 0, 0):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
            print()
    else:
        print("No solution found.")

board = [[1, 0, 8, 5, 3, 0, 6, 0, 0],
         [0, 2, 0, 0, 0, 1, 0, 0, 0],
         [0, 4, 0, 0, 0, 0, 0, 0, 8],
         [8, 0, 5, 0, 0, 3, 0, 0, 9],
         [0, 0, 4, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 0, 2, 0, 0],
         [3, 0, 9, 0, 0, 5, 0, 0, 2],
         [0, 0, 0, 6, 0, 0, 0, 7, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0]]
