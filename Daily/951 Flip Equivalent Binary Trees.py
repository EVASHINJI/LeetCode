# Url: https://leetcode.com/problems/flip-equivalent-binary-trees/
# Related Topics:
# Tree

# Example:
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
            return True
        if self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left):
            return True
        return False