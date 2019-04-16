def minPathSum(self, grid: List[List[int]]) -> int:
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    my_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

    my_grid[0][0] = grid[0][0]
    for i in range(1, len(grid)):
        my_grid[i][0] = grid[i][0] + my_grid[i - 1][0]
    for i in range(1, len(grid[0])):
        my_grid[0][i] = grid[0][i] + my_grid[0][i - 1]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            my_grid[i][j] = min(my_grid[i - 1][j], my_grid[i][j - 1]) + grid[i][j]
    return my_grid[-1][-1]