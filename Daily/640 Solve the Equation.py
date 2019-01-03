# Url: https://leetcode.com/problems/solve-the-equation/
# Related Topics:
# Math

# Example:
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
# Input: "x=x"
# Output: "Infinite solutions"
# Input: "x=x+2"
# Output: "No solution"


class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def parse(s):
            coe, num = 0, 0
            tmp = ""
            for c in s+'+':
                if c == 'x':
                    if not tmp or not tmp[0].isdigit() and len(tmp) == 1:
                        tmp += '1'
                    coe += int(tmp)
                    tmp = ""
                elif c in '+-':
                    if not tmp:
                        tmp = '0'
                    num += int(tmp)
                    tmp = c
                else:
                    tmp += c
            return coe, num
        
        subs = equation.split('=')
        coe_left, num_left = parse(subs[0])
        coe_right, num_right = parse(subs[1])
        if coe_left == coe_right:
            if num_left == num_right:
                return "Infinite solutions"
            else:
                return "No solution"
        return 'x=%d' % ((num_right - num_left) / (coe_left - coe_right))