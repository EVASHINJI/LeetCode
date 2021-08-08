// Url: https://leetcode.com/problems/palindrome-partitioning/
// Related Topics:
// DP String Backtracking

// Example 1:
// Input: s = "aab"
// Output: [["a","a","b"],["aa","b"]]

// Example 2:
// Input: s = "a"
// Output: [["a"]]

class Solution {
    public void backtrack(List<List<String>> results, List<String> arr, boolean[][] dp, String s, int start) {
        if (start == s.length()) results.add(new ArrayList<>(arr));
        for (int end = start; end < s.length(); end++) {
            if (s.charAt(start) == s.charAt(end) && (end - start <= 2 || dp[start+1][end-1])) {
                dp[start][end] = true;
                arr.add(s.substring(start, end + 1));
                backtrack(results, arr, dp, s, end + 1);
                arr.remove(arr.size() - 1);
            }
        }
    }

    public List<List<String>> partition(String s) {
        List<List<String>> results = new ArrayList<>();
        List<String> arr = new ArrayList<>();
        boolean[][] dp = new boolean[s.length()][s.length()];
        backtrack(results, arr, dp, s, 0);
        return results;
    }
}