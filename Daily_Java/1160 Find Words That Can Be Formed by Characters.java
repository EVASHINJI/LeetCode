// Url: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
// Related Topics:
// Array HashTable String

// Example 1:
// Input: words = ["cat","bt","hat","tree"], chars = "atach"
// Output: 6
// Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

// Example 2:
// Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
// Output: 10
// Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

class Solution {
    public boolean check(String word, int[] dict) {
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (dict[idx] <= 0) return false;
            dict[idx]--;
        }
        return true;
    }

    public int countCharacters(String[] words, String chars) {
        int[] dict = new int[26];
        for (char c : chars.toCharArray()) {
            dict[c - 'a']++;
        }
        int ans = 0;
        for (String word : words) {
            if (check(word, Arrays.copyOf(dict, dict.length))) ans += word.length();
        }
        return ans;
    }
}