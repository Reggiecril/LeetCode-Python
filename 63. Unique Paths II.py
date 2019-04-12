def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid[0])
    n = len(obstacleGrid)
    if obstacleGrid[0][0] == 1:
        return 0
    value = 1
    for i in range(m):
        if obstacleGrid[0][i] == 1:
            value = 0
        obstacleGrid[0][i] = value
    value = 1
    for i in range(1, n):
        if obstacleGrid[i][0] == 1:
            value = 0
        obstacleGrid[i][0] = value
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[j][i] == 1:
                obstacleGrid[j][i] = 0
            else:
                obstacleGrid[j][i] = obstacleGrid[j - 1][i] + obstacleGrid[j][i - 1]

    return obstacleGrid[-1][-1]