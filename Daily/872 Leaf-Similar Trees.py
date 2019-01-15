# Url: https://leetcode.com/problems/leaf-similar-trees/
# Related Topics:
# Tree DepthFirstSearch

# Example:


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leafSequence(root1) == self.leafSequence(root2)
    
    def leafSequence(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.leafSequence(root.left) + self.leafSequence(root.right)