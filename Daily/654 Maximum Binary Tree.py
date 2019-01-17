# Url: https://leetcode.com/problems/maximum-binary-tree/
# Related Topics:
# Tree

# Example:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:

#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def construct(l, r):
            if l == r:
                return None
            ma_idx = l
            for i in range(l+1, r):
                if nums[i] > nums[ma_idx]:
                    ma_idx = i
            node = TreeNode(nums[ma_idx])
            node.left = construct(l, ma_idx)
            node.right = construct(ma_idx + 1, r)
            return node
        
        return construct(0, len(nums))