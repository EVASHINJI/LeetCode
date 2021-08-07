// Url: https://leetcode.com/problems/surrounded-regions/
// Related Topics:
// Array DepthFirstSearch BreadthFirstSearch UnionFind Matrix

// Example 1:
// Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
// Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
// Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

// Example 2:
// Input: board = [["X"]]
// Output: [["X"]]

class Solution {
    public void solve(char[][] board) {
        int[][] deltas = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int rows = board.length;
        int cols = board[0].length;
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < rows; i++) {
            if (board[i][0] == 'O') q.offer(new int[]{i, 0});
            if (board[i][cols - 1] == 'O') q.offer(new int[]{i, cols-1});
        }
        for (int j = 0; j < cols; j++) {
            if (board[0][j] == 'O') q.offer(new int[]{0, j});
            if (board[rows-1][j] == 'O') q.offer(new int[]{rows-1, j});
        }
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            if (r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] != 'O') continue;
            board[r][c] = 'B';
            for (int[] delta : deltas) {
                q.offer(new int[]{r+delta[0], c+delta[1]});
            }
        }
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == 'B') board[i][j] = 'O';
                else board[i][j] = 'X';
            }
        }
    }
}