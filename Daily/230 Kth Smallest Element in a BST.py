# Url: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Related Topics:
# Tree BinarySearch

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = None
        seen, q = set(), [root]
        while q:
            node = q.pop()
            if not node:
                continue
            if node in seen:
                if k == 1:
                    return node.val
                k -= 1
                continue
            q.extend([node.right, node, node.left])
            seen.add(node)