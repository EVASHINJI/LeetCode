# Url: https://leetcode.com/problems/subtree-of-another-tree/
# Related Topics:
# Tree

# Example 1:
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.isSubtreeWithFlag(s, t, True)
        
    
    def isSubtreeWithFlag(self, s, t, isRoot):
        if (not s)^(not t):
            return False
        else:
            if not s:
                return True
            if s.val == t.val:
                if self.isSubtreeWithFlag(s.left, t.left, False) and self.isSubtreeWithFlag(s.right, t.right, False):
                    return True
            elif not isRoot:
                return False
            if self.isSubtreeWithFlag(s.left, t, True) or self.isSubtreeWithFlag(s.right, t, True):
                return True
            return False