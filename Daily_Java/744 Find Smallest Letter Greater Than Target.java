// Url: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
// Related Topics:
// Array BinarySearch

// Example 1:
// Input: letters = ["c","f","j"], target = "a"
// Output: "c"

// Example 2:
// Input: letters = ["c","f","j"], target = "c"
// Output: "f"

// Example 3:
// Input: letters = ["c","f","j"], target = "d"
// Output: "f"

class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int l = 0;
        int r = letters.length;
        while (l < r) {
            int mid = (l + r) / 2;
            char letter = letters[mid];
            if (letter > target) r = mid;
            else l = mid + 1;
        }
        if (r == letters.length) return letters[0];
        return letters[r];
    }
}