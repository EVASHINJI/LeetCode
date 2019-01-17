# Url: https://leetcode.com/problems/all-possible-full-binary-trees/
# Related Topics:
# Tree Recursion

# Example:
# Input: 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.memo = {1: [TreeNode(0)]}
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        if N not in self.memo:
            ans = []
            for i in range(1, N, 2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N - 1 - i):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        ans.append(node)
            self.memo[N] = ans
        return self.memo[N]