// Url: https://leetcode.com/problems/number-of-islands/
// Related Topics:
// Array DepthFirstSearch BreadthFirstSearch UnionFind Matrix

// Example 1:
// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1

// Example 2:
// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3

class Solution {
    public void occupyIsland(char[][] grid, int[][] island, int i, int j, int islandNo) {
        if (i >= 0 && i < grid.length && j >= 0 && j < grid[0].length 
                && island[i][j] == 0 && grid[i][j] == '1') {
            island[i][j] = islandNo;
            occupyIsland(grid, island, i+1, j, islandNo);
            occupyIsland(grid, island, i-1, j, islandNo);
            occupyIsland(grid, island, i, j+1, islandNo);
            occupyIsland(grid, island, i, j-1, islandNo);
        }
    }

    public int numIslands(char[][] grid) {
        int[][] island = new int[grid.length][grid[0].length];
        int inlandNum = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '0' || island[i][j] > 0) continue;
                occupyIsland(grid, island, i, j, ++inlandNum);
            }
        }
        return inlandNum;
    }
}