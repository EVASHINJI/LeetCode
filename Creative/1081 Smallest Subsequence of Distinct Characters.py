# Url: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# Related Topics:
# String

# Example 1:
# Input: "cdadabcc"
# Output: "adbc"

# Example 2:
# Input: "abcd"
# Output: "abcd"

# Example 3:
# Input: "ecbacba"
# Output: "eacb"

# Creative
# Stack can find the inc or dec order in arr


class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last_pos = {c: i for i, c in enumerate(text)}
        stack = []
        for i, c in enumerate(text):
            if c in stack: continue
            while stack and c < stack[-1] and i < last_pos[stack[-1]]:
                stack.pop()
            stack.append(c)
        return ''.join(stack)