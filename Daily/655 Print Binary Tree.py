# Url: https://leetcode.com/problems/print-binary-tree/
# Related Topics:
# Tree

# Example 1:
# Input:
#      1
#     / \
#    2   3
#     \
#      4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# Example 2:
# Input:
#       1
#      / \
#     2   5
#    / 
#   3 
#  / 
# 4 
# Output:
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        traverse, line = [], [root]
        while True:
            traverse.append(line)
            nxt = []
            empty_num = 0
            for node in line:
                if node and (node.left or node.right):
                    nxt.extend([node.left, node.right])
                else:
                    empty_num += 2
                    nxt.extend([None, None])
            if empty_num == 2*len(line):
                break
            line = nxt
        depth = len(traverse)
        cols = 2**(depth-1) - 1
        ans = []
        for i in range(depth):
            line = []
            padding = [""]*(2**(depth - i - 1) - 1)
            for node in traverse[i]:
                if line:
                    line.append("")
                if node:
                    line.extend(padding + [str(node.val)] + padding)
                else:
                    line.extend(padding+ [""] + padding)
            ans.append(line)
        return ans