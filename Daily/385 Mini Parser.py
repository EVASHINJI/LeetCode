# Url: https://leetcode.com/problems/mini-parser/
# Related Topics:
# String Stack

# Example:
# Given s = "[123,[456,[789]]]",
# Return a NestedInteger object containing a nested list with 2 elements:
# 1. An integer containing value 123.
# 2. A nested list containing two elements:
#     i.  An integer containing value 456.
#     ii. A nested list with one element:
#          a. An integer containing value 789.


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        num = ''
        def update(stack, elem):
            nested = stack[-1]
            nested.add(elem)
        
        stack, ans = [], None
        for c in s:
            if c == '[':
                stack.append(NestedInteger())
            elif c == ']':
                if num:
                    update(stack, int(num))
                    num = ''
                elem = stack.pop()
                if stack:
                    update(stack, elem)
                else:
                    return elem
            elif c == ',':
                if num:
                    update(stack, int(num))
                    num = ''
            else:
                num += c
        return NestedInteger(int(num))