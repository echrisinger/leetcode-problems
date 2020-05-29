class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        if rows == 1 or cols == 1:
            return 1 if all([not any(row) for row in obstacleGrid])\
                   else 0
        
        for i in range(rows):
            for j in range(cols):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] else 1
        
        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 0:
                    continue
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
        return obstacleGrid[-1][-1]

# O(nm), O(1)
