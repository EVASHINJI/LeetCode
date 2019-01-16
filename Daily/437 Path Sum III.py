# Url: https://leetcode.com/problems/path-sum-iii/
# Related Topics:
# Tree

# Example:
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, k):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.ans = 0
        def pathSumValues(root):
            if not root:
                return []
            candidates = pathSumValues(root.left) + pathSumValues(root.right) + [0]
            path_sum_values = []
            for cand in candidates:
                add = cand + root.val
                if add == k:
                    self.ans += 1
                path_sum_values.append(add)
            return path_sum_values
        
        pathSumValues(root)
        return self.ans