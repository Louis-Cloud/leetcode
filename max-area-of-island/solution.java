class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        // Holds max area of island
        int max = 0;
        
        // Iterate through 2d array
        for(int j = 0; j < grid[0].length; j++) {
            for(int i = 0; i < grid.length; i++) {
                // Grab element value
                int cell = grid[i][j];
                // If cell is alive
                if(cell > 0) {
                    if(i > 0) {
                        // If left neigbor is alive, add neighbor amount to self
                        if(grid[i - 1][j] > 0) {            
                            grid[i][j] += grid[i - 1][j];
                        }
                        // If not, see if left neighbor beats the max value
                        else {
                            max = Math.max(max, grid[i - 1][j] * -1);
                        }
                    }
                    // If above neighbor is negative, add it to self
                    if(j > 0 && grid[i][j - 1] < 0) {
                        grid[i][j] += grid[i][j - 1] * -1;
                    }
                } 
                // If cell is dead
                else if(cell == 0) {
                    if(i > 0) {
                        // if left neighbor is alive, carry negative value of that
                        if(grid[i - 1][j] > 0) {
                            grid[i][j] = -1 * grid[i - 1][j];
                        }
                        // if not, then inherit whatever value it is
                        else {
                            grid[i][j] = grid[i - 1][j];
                        }
                        
                    }
                }
                // If cell is negative
                else {
                    if(j > 0) {
                        
                        if(grid[i][j - 1] <= 0) {
                            // If above neighbor is less than 0
                            if(grid[i][j - 1] < 0) {
                                // Add it to current value
                                grid[i][j] += grid[i][j - 1];
                            }
                            // If above neighbor was negative, 
                            // then set top right neighbor to 0, 
                            // if that was also negative
                            if(i < grid.length - 1 && grid[i + 1][j - 1] < 0) {
                                grid[i + 1][j - 1] = 0;
                            }
                        }
                    }
                }
                // If at the end of the row, see if whatever value you have is the max
                if(i == grid.length - 1) {
                    max = Math.max(max,Math.abs(grid[i][j]));
                }
            }
        }
        return max;
    }
}