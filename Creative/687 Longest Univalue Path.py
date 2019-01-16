# Url: https://leetcode.com/problems/longest-univalue-path/
# Related Topics:
# Tree Recursion

# Example 1:
# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2
# Example 2:
# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2

# Creative/Notice
# Remember to judge if the left(right)_arrow can be connected with left(right)_len
# Can't plus one roughly.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path_len = 0
        def UnivaluePath(root):
            if not root:
                return 0
            left_len = UnivaluePath(root.left)
            right_len = UnivaluePath(root.right)
            left_arrow = right_arrow = 0
            if root.left and root.left.val == root.val:
                left_arrow = left_len + 1
            if root.right and root.right.val == root.val:
                right_arrow = right_len + 1
            self.max_path_len = max(self.max_path_len, left_arrow + right_arrow)
            
            return max(left_arrow, right_arrow)
            
        UnivaluePath(root)
        return self.max_path_len