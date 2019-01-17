# Url: https://leetcode.com/problems/binary-tree-pruning/
# Related Topics:
# Tree

# Example:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1] 
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def if_prune(node):
            if not node:
                return True
            if node.left and if_prune(node.left):
                node.left = None
            if node.right and if_prune(node.right):
                node.right = None
            if not node.left and not node.right and node.val == 0:
                return True
            return False
        
        if_prune(root)
        return root