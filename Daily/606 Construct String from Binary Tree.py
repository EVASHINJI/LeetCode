# Url: https://leetcode.com/problems/construct-string-from-binary-tree/
# Related Topics:
# String Tree

# Example:
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /    
#   4     

# Output: "1(2(4))(3)"


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        left = '(%s)' % self.tree2str(t.left) if t.left or t.right else ''
        right = '(%s)' % self.tree2str(t.right) if t.right else ''
        return '%s%s%s' % (str(t.val), left, right)
        