# N is the size of the 2D matrix N*N
N = 9

# A utility function to print grid
def printing(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end = " ")
		print()

# Checks whether it will be legal to assign number to the given row, col
def isSafe(grid, row, col, num):

	# Check if the same number is in same row, return false!
	for x in range(9):
		if grid[row][x] == num:
			return False

	# Check if the same number is in same column, return false!
	for x in range(9):
		if grid[x][col] == num:
			return False

	# Check if the same number is in the same 3*3 matrix, return false
	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

# Takes a partially filled-in grid and attempts to assign values to all unassigned locations in such a way to meet the requirements for Sudoku solution (non-duplication across rows,columns, and boxes) */
def solveSuduko(grid, row, col):

	# Check if reached the 8th row and 9th column (0 indexed matrix), then returning true to avoid further backtracking
	if (row == N - 1 and col == N):
		return True
	
	# Check if column value becomes 9, then move to next row and column start from 0
	if col == N:
		row += 1
		col = 0

	# Check if the current position of the grid already contains value > 0, then iterate for next column
	if grid[row][col] > 0:
		return solveSuduko(grid, row, col + 1)
	for num in range(1, N + 1, 1):
	
  # Check if it is safe to place the number (1-9) in the given row ,col -> move to next column
		if isSafe(grid, row, col, num):
		
	# Assigning the number in the current (row,col) position of the grid and assuming the assined number in the position is correct
			grid[row][col] = num

	# Checking for next possibility with next column
			if solveSuduko(grid, row, col + 1):
				return True

	# Removing the assigned number, since the assumption was wrong, and go for next assumption with different number value
		grid[row][col] = 0
	return False

# Driver Code

# 0 means unassigned cells
grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

if (solveSuduko(grid, 0, 0)):
	printing(grid)
else:
	print("no solution")

# SUDOKU SOLVED!!
