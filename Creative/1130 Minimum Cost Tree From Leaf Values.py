# Url: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# Related Topics:
# DP Stack Tree

# Example 1:
# Input: arr = [6,2,4]
# Output: 32
# Explanation:
# There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.
#     24            24
#    /  \          /  \
#   12   4        6    8
#  /  \               / \
# 6    2             2   4

# Creative
# Don't be limited in DP think more


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        ans = 0
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                ans += mid*min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
        return ans
        
        