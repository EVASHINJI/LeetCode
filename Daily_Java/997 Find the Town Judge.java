// Url: https://leetcode.com/problems/find-the-town-judge/
// Related Topics:
// Array HashTable Graph

// Example 1:
// Input: n = 2, trust = [[1,2]]
// Output: 2

// Example 2:
// Input: n = 3, trust = [[1,3],[2,3]]
// Output: 3

// Example 3:
// Input: n = 3, trust = [[1,3],[2,3],[3,1]]
// Output: -1

// Example 4:
// Input: n = 3, trust = [[1,2],[2,3]]
// Output: -1

// Example 5:
// Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
// Output: 3

class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] beTrusted = new int[n + 1];
        for (int i = 0; i < trust.length; i++) {
            int ai = trust[i][0];
            int bi = trust[i][1];
            beTrusted[ai]--;
            beTrusted[bi]++;
        }
        for (int i = 1; i <= n; i++) {
            if (beTrusted[i] == n - 1) return i;
        }
        return -1;
    }
}