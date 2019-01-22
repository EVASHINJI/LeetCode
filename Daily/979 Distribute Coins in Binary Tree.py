# Url: https://leetcode.com/problems/distribute-coins-in-binary-tree/
# Related Topics:
# Tree DepthFirstSearch

# Example:
# Input: [0,3,0]
# Output: 3
# Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.traverse(root)
        return self.ans
        
    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.ans += abs(left) + abs(right)
        return root.val + left + right - 1
        