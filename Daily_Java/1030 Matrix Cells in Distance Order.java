// Url: https://leetcode.com/problems/matrix-cells-in-distance-order/
// Related Topics:
// Array Math Sorting Geometry Matrix

// Example 1:
// Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
// Output: [[0,0],[0,1]]
// Explanation: The distances from (0, 0) to other cells are: [0,1]

// Example 2:
// Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
// Output: [[0,1],[0,0],[1,1],[1,0]]
// Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
// The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

// Example 3:
// Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
// Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
// Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
// There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

class Solution {
    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        boolean[][] visit = new boolean[rows][cols];
        int[][] deltas = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        int[][] ans = new int[rows * cols][2];
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{rCenter, cCenter});
        int i = 0;
        while (!q.isEmpty()) {
            int[] curPos = q.poll();
            int r = curPos[0], c = curPos[1];
            if (r < 0 || r >= rows || c < 0 || c >= cols || visit[r][c]) continue;
            ans[i] = curPos;
            i++;
            visit[r][c] = true;
            for (int[] delta: deltas) {
                q.offer(new int[] {r + delta[0], c + delta[1]});
            }
        }
        return ans;
    }
}