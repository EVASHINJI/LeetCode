# Url: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Related Topics:
# Tree

# Example:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        ans, line = [], [root]
        while line:
            next_line, line_val = [], []
            for item in line:
                line_val.append(item.val)
                if item.left: next_line.append(item.left)
                if item.right: next_line.append(item.right)
            ans.append(float(sum(line_val))/ len(line_val))
            line = next_line
        return ans