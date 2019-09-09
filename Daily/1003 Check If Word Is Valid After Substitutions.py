# Url: https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
# Related Topics:
# String Stack

# Example 1:
# Input: "aabcbc"
# Output: true
# Explanation: 
# We start with the valid string "abc".
# Then we can insert another "abc" between "a" and "bc", resulting in "a" + "abc" + "bc" which is "aabcbc".

# Example 2:
# Input: "abcabcababcc"
# Output: true
# Explanation: 
# "abcabcabc" is valid after consecutive insertings of "abc".
# Then we can insert "abc" before the last letter, resulting in "abcabcab" + "abc" + "c" which is "abcabcababcc".

# Example 3:
# Input: "abccba"
# Output: false


class Solution:
    def isValid(self, S: str) -> bool:
        if not S or len(S) % 3 or S[0] != 'a' or S[-1] != 'c':
            return False
        stack = []
        for ch in S:
            if ch == 'c':
                if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                    continue
            stack.append(ch)
        return False if stack else True