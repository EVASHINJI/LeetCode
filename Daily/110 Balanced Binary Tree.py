# Url: https://leetcode.com/problems/balanced-binary-tree/
# Related Topics:
# Tree DepthFirstSearch

# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example:
# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = True
        def treeHeight(root):
            if not root or not self.ans:
                return 0
            left = treeHeight(root.left) + 1
            right = treeHeight(root.right) + 1
            if abs(left - right) > 1:
                self.ans = False
            return max(left, right)
        
        treeHeight(root)
        return self.ans