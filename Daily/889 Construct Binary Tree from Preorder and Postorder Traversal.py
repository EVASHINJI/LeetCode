# Url: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# Related Topics:
# Tree

# Example:
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        idx = post.index(pre[1]) + 1
        node = TreeNode(pre[0])
        node.left = self.constructFromPrePost(pre[1:idx+1], post[:idx])
        node.right = self.constructFromPrePost(pre[idx+1:], post[idx:-1])
        return node