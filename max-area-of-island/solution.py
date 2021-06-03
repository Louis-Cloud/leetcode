class Solution(object):
    def maxAreaOfIsland(self, grid):
        max_area = 0
        
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i > 0 and grid[i - 1][j] > 0 and j < n - 1 and grid[i - 1][j + 1] == 0) or (i > 0 and grid[i - 1][j] > 0 and j == n):
                        print("HA")
                        grid[i][j] += grid[i - 1][j]
                    if j > 0:
                        print("HIT")
                        grid[i][j] += grid[i][j - 1]
                        if j == n - 1 or grid[i][j + 1] == 0:
                            for k in range(grid[i][j]):
                                grid[i][j - k - 1] = grid[i][j]
                            max_area = max(grid[i][j],max_area)
                print(str(i) + "," + str(j))
                print("max: " + str(max_area))
                for row in grid:
                    print(row)
        return max_area