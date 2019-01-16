# Url: https://leetcode.com/problems/binary-tree-tilt/
# Related Topics:
# Tree

# Example:
# Input: 
#          1
#        /   \
#       2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.treeSum(root)
        return self.sum
            
    def treeSum(self, root):
        if not root:
            return 0
        left_sum = self.treeSum(root.left)
        right_sum = self.treeSum(root.right)
        self.sum += abs(left_sum - right_sum)
        return root.val + left_sum + right_sum