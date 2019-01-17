# Url: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Related Topics:
# Tree Stack HashTable

# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,3,2]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, seen = [], set()
        traversed = [root]
        while traversed:
            node = traversed.pop()
            if not node:
                continue
            if node in seen:
                ans.append(node.val)
            else:
                traversed.extend([node.right, node, node.left])
                seen.add(node)
        return ans