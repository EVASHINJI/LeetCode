# Url: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Related Topics:
# Tree

# Example 1:
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def traverse(node, val):
            nxt_val = (val << 1) + node.val
            if not node.left and not node.right:
                return nxt_val
            left, right = 0, 0
            if node.left: left = traverse(node.left, nxt_val)
            if node.right: right = traverse(node.right, nxt_val)
            return left + right
        
        return traverse(root, 0)