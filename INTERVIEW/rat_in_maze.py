n = 4


def isvalid(n, maze, x, y, res):  # res refers to solution path
    # here maze[x][y]==1 means if the cell is open and about res it means the cell has not been included in the current path yet
    if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0:
        return True
    return False


def RatMaze(n, maze, move_x, move_y, x, y, res):
    if x == n-1 and y == n-1:       # if the current is the goal
        return True
    for i in range(4):  # 4 moves totally
        x_new = x+move_x[i]
        y_new = y+move_y[i]

        if isvalid(n, maze, x_new, y_new, res):  # if move to new coordinates is valid
            res[x_new][y_new] = 1   # if valid it is marked as 1

            # recursive calling of RataMaze for the new coordinates
            if RatMaze(n, maze, move_x, move_y, x_new, y_new, res):
                return True  # true if a path to goal is found
            res[x_new][y_new] = 0   # if no path is found mark the cells as zero
    return False    # if no path is found then false


def solveMaze(maze):    # for 2d matrix
    res = [[0 for i in range(n)] for i in range(n)]
    res[0][0] = 1   # initialize the starting cell as 1

    # movement vectors for possible moves up,down,right,left
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]

    # searching for a path from start of cell, a cell marked as 1 is part of the cell and zero is not part of the cell
    if RatMaze(n, maze, move_x, move_y, 0, 0, res):
        for i in range(n):
            for j in range(n):
                print(res[i][j], end=" ")
            print()
    else:
        print('Solution does not exist')


maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

solveMaze(maze)
