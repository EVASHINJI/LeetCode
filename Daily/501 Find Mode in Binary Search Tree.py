# Url: https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Related Topics:
# Tree

# Example:
# Given BST [1,null,2,2],
#    1
#     \
#      2
#     /
#    2
# return [2].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        def traverse(root):
            if not root:
                return []
            return traverse(root.left) + [root.val] + traverse(root.right)
        
        nums = traverse(root)
        nums += [nums[0] - 1]
        pos, mode_len = 0, 1
        ans = []
        for i in range(1, len(nums)):
            if nums[i] != nums[pos]:
                if i - pos > mode_len:
                    ans = [nums[i-1]]
                    mode_len = i - pos
                elif i - pos == mode_len:
                    ans.append(nums[i-1])
                pos = i
        return ans