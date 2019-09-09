# Url: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Related Topics:
# Tree Recursion

# Example :
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
#           4
#         /   \
#        2     6
#       / \    
#      1   3  
# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        path = []
        def inorder(node):
            if node.left: inorder(node.left)
            path.append(node.val)
            if node.right: inorder(node.right)
        
        inorder(root)
        return min([abs(a-b) for a, b in zip(path, path[1:])])