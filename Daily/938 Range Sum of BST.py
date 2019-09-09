# Url: https://leetcode.com/problems/range-sum-of-bst/
# Related Topics:
# Tree Recursion

# Example 1:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if L <= node.val <= R:
                ans += node.val
            if L < node.val:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
        return ans