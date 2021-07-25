// Url: https://leetcode.com/problems/flood-fill/
// Related Topics:
// Array DepthFirstSearch BreadthFirstSearch Matrix

// Example 1:
// Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
// Output: [[2,2,2],[2,2,0],[2,0,1]]
// Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
// Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

// Example 2:
// Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
// Output: [[2,2,2],[2,2,2]]


class Solution {
    public static final int[] deltaR = {-1, 1, 0, 0};
    public static final int[] deltaC = {0, 0, -1, 1};

    public boolean valid(int[][] image, int nr, int nc) {
        return nr >= 0 && nr < image.length && nc >=0 && nc < image[0].length;
    }

    public void dfs(int[][] image, int sr, int sc, int oldColor, int newColor) {
        if (!valid(image, sr, sc) || image[sr][sc] != oldColor) return;
        image[sr][sc] = newColor;
        dfs(image, sr + 1, sc, oldColor, newColor);
        dfs(image, sr - 1, sc, oldColor, newColor);
        dfs(image, sr, sc + 1, oldColor, newColor);
        dfs(image, sr, sc - 1, oldColor, newColor);
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if (image[sr][sc] == newColor) return image;
        dfs(image, sr, sc, image[sr][sc], newColor);
        return image;
    }
}