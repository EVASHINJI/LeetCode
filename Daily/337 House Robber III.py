# Url: https://leetcode.com/problems/house-robber-iii/
# Related Topics:
# Tree DepthFirstSearch

# Example 1:
# Input: [3,2,3,null,3,null,1]
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

# Example 2:
# Input: [3,4,5,1,3,null,1]
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def choice(root):
            if not root:
                return [0, 0]
            left = choice(root.left)
            right = choice(root.right)
            now = left[1] + right[1] + root.val
            later = max(left) + max(right)
            return [now, later]  
        return max(choice(root))
                