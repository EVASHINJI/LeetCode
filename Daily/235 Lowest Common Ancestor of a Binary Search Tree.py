# Url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Related Topics:
# Tree

# Example:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = self.findPath(root, p.val)
        q_path = self.findPath(root, q.val)
        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            i += 1
        return p_path[i-1]
    
    def findPath(self, root, val):
        if val == root.val:
            return [root]
        elif val > root.val:
            return [root] + self.findPath(root.right, val)
        else:
            return [root] + self.findPath(root.left, val)