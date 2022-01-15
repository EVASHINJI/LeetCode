// Url: https://leetcode.com/problems/remove-duplicate-letters/
// Related Topics:
// String Stack MonotonicStack Greedy

// Example 1:
// Input: s = "bcabc"
// Output: "abc"

// Example 2:
// Input: s = "cbacdcbc"
// Output: "acdb"

class Solution {
    public String removeDuplicateLetters(String s) {
        int[] lastPos = new int[26];
        boolean[] seen = new boolean[26];
        for (int i = 0; i < s.length(); i++) {
            lastPos[s.charAt(i) - 'a'] = i;
        }
        Deque<Character> stack = new LinkedList<>();
        for (int i = 0; i < s.length(); i++) {
            if (seen[s.charAt(i)-'a']) continue;
            while (!stack.isEmpty()
                    && s.charAt(i) < stack.peek()
                    && lastPos[stack.peek() - 'a'] > i) {
                seen[stack.pop()-'a'] = false;
            }
            stack.push(s.charAt(i));
            seen[s.charAt(i)-'a'] = true;
        }
        StringBuilder stringBuilder = new StringBuilder();
        while (!stack.isEmpty()) {
            stringBuilder.append(stack.pop());
        }
        return stringBuilder.reverse().toString();
    }
}