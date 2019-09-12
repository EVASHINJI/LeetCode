# Url: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Related Topics:
# Tree

# Example 1:
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        i = 1
        while i < len(preorder) and preorder[i] < preorder[0]:
            i += 1
        node = TreeNode(preorder[0])
        node.left = self.bstFromPreorder(preorder[1:i])
        node.right = self.bstFromPreorder(preorder[i:])
        return node