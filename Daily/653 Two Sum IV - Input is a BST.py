# Url: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Related Topics:
# Tree

# Example:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 9
# Output: True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        want = set()
        q = [root]
        while q:
            node = q.pop()
            if node.val in want:
                return True
            want.add(k - node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return False