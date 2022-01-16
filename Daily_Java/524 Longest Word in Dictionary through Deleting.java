// Url: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
// Related Topics:
// Array TwoPointers String Sorting

// Example 1:
// Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
// Output: "apple"

class Solution1 {
    public boolean check(String s, String word) {
        int p1 = 0;
        int p2 = 0;
        while (p1 < s.length() && p2 < word.length()) {
            if (s.charAt(p1) == word.charAt(p2)) {
                p2++;
            }
            p1++;
        }
        return p2 == word.length();
    }

    public String findLongestWord(String s, List<String> dictionary) {
        dictionary.sort((d1, d2) -> {
            if (d1.length() != d2.length()) {
                return d2.length() - d1.length();
            }
            return d1.compareTo(d2);
        });
        for (String word : dictionary) {
            if (check(s, word)) return word;
        }
        return "";
    }
}

class Solution2 {
    public String findLongestWord(String s, List<String> dictionary) {
        int[][] dp = new int[s.length()+1][26];
        Arrays.fill(dp[s.length()], s.length());
        // 构造动态规划数组
        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = 0; j < 26; j++) {
                char c = (char)('a' + j);
                if (s.charAt(i) == c) {
                    dp[i][j] = i;
                } else {
                    dp[i][j] = dp[i+1][j];
                }
            }
        }

        // 字典排序
        dictionary.sort((d1, d2) -> {
            if (d1.length() != d2.length()) {
                return d2.length() - d1.length();
            }
            return d1.compareTo(d2);
        });

        for (String word : dictionary) {
            int p1 = 0;
            int p2 = 0;
            while (p2 < word.length()) {
                p1 = dp[p1][word.charAt(p2)-'a'];
                if (p1 == s.length()) break;
                p1++;
                p2++;
            }
            if (p2 == word.length()) return word;
        }
        return "";
    }
}