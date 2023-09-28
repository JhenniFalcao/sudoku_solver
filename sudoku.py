import pyautogui as pg 
import numpy as np
import time

# represents our Sudoku, which will be a list of lists.
grid = []

while True:
    row = list(input('Row: ')) # is the input for manually filling in the rows of the Sudoku.
    ints = [] 

    for n in row:
        ints.append(int(n)) # this will iterate through each number in the line and then convert it to int
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')

time.sleep(3) # pause the program for 3 seconds

def possible(x, y, n):
    # n is the possible number

    # step 1: check the number in the rows and columns (respectively) (x = rows, y = columns)

    for i in range(0, 9):
        if grid[i][x] == n and i != y: # Checks for number (n) in X rows
            return False

    for i in range(0, 9):
        if grid[y][i] == n and i != x: # Checks for number (n) in Y columns
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  # Checks for numbers in box(no matter the position, it finds the corner)
            if grid[Y][X] == n:
                return False 
    '''
    This logic ensures that the number is not present in the 3x3 subgrid that contains the cell. It checks the numbers within the box.
    '''   
    return True

def Print(matrix):
    final = []
    str_fin = []

    # Iterate through indices 0 to 8 (representing rows) and append each row to 'final'
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = [] # Initialize a counter list to keep track of printed numbers

    for num in str_fin:
        pg.press(num) # Simulate pressing the current number
        pg.hotkey('right') # Simulate moving the cursor right
        counter.append(num)
        
        if len(counter)%9 == 0:
            pg.hotkey('down') # Simulate moving the cursor down to the next row
            for i in range(8): # Simulate moving the cursor left 8 times to return to the first position of the next row
                pg.hotkey('left')


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0: # If the current cell is empty (0)
                # Try numbers from 1 to 9 to find a valid solution
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0 # Backtrack by resetting the cell to 0 if the solution was not found
                return # Return to the previous recursive call
    Print(grid)
    input("More?")

solve()