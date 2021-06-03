"""
Returns area of island given the coordinate of one of its live cells using recursion

Parameters:
----------
i:      row index of grid
j:      column index of grid
grid:   2d array of grid. Function takes advantage of Python's pass by reference.
"""
def getArea(i, j, grid):
        if  i < 0 or i >= len(grid) or      # If j index is out of range OR
            j < 0 or j >= len(grid[0]) or   # k index is out of range OR
            grid[i][j] == 0:                # cell is 0 THEN
            return 0                        # return area = 0
        
        grid[i][j] = 0                      # Set area to 0 so cell won't be double counted
        
        return  1 +                         # Area of current cell
                getArea(i - 1, j, grid) +   # Finds area of above cell and its neighbors
                getArea(i, j - 1, grid) +   # Finds area of left cell and its neighbors
                getArea(i + 1, j, grid) +   # Finds area of below cell and its neighbors
                getArea(i, j + 1, grid)     # Finds area of right cell and its neighbors

class Solution(object):
    def maxAreaOfIsland(self, grid):
        max_area = 0                        # Holds max area
        
        m = len(grid)                       # Gets height of grid
        n = len(grid[0])                    # Gets width of grid
        for i in range(m):                  # Loops through rows
            for j in range(n):              # Loops through columns
                if grid[i][j] == 1:         # If cell is live
                    # Get the area of island and see if it is the max
                    max_area = max(max_area, getArea(i,j,grid))  
        return max_area                     # Return answer