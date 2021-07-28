// Url: https://leetcode.com/problems/number-of-lines-to-write-string/
// Related Topics:
// Array String 

// Example 1:
// Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
// Output: [3,60]
// Explanation: You can write s as follows:
// abcdefghij  // 100 pixels wide
// klmnopqrst  // 100 pixels wide
// uvwxyz      // 60 pixels wide
// There are a total of 3 lines, and the last line is 60 pixels wide.

// Example 2:
// Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
// Output: [2,4]
// Explanation: You can write s as follows:
// bbbcccdddaa  // 98 pixels wide
// a            // 4 pixels wide
// There are a total of 2 lines, and the last line is 4 pixels wide.

class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int current_width = 0;
        int line = 1;
        for (char c : s.toCharArray()) {
            int width = widths[c - 'a'];
            if (current_width + width > 100) {
                line += 1;
                current_width = width;
            } else {
                current_width += width;
            }
        }
        return new int[]{line, current_width};
    }
}