# Url: https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
# Related Topics:
# Tree Math

# Example 1:
# Input: label = 14
# Output: [1,3,4,14]

# Example 2:
# Input: label = 26
# Output: [1,2,6,10,26]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        order = []
        while label:
            order.append(label)
            label = label // 2
        ans = []
        l = len(order)
        for i in range(l):
            num = pow(2, l - i - 1) * 3 - 1 - order[i] if i % 2 else order[i]
            ans.append(num)
        return ans[::-1]