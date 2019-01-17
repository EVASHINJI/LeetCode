# Url: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Related Topics:
# Tree

# Example:
# Input: [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        parent = {}
        line = [root]
        while True:
            next_line = []
            for node in line:
                if node.left: 
                    next_line.append(node.left)
                    parent[node.left] = node
                if node.right:
                    next_line.append(node.right)
                    parent[node.right] = node
            if not next_line:
                break
            line = next_line
        line = set(line)
        while len(line) > 1:
            pre_node = set()
            for node in line:
                pre_node.add(parent[node])
            line = pre_node
        return list(line)[0]