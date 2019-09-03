# Url: https://leetcode.com/problems/binary-tree-postorder-traversal/
# Related Topics:
# Stack Tree

# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [3,2,1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [(root, False)]
        ans = []
        while stack:
            while stack and stack[-1][1]:
                node, seen = stack.pop()
                ans.append(node.val)
            if stack:
                node, seen = stack.pop()
                stack.append((node, True))
                if node.right: stack.append((node.right, False))
                if node.left: stack.append((node.left, False))
        return ans