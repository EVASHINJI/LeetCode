# Url: https://leetcode.com/problems/fraction-addition-and-subtraction/
# Related Topics:
# Math

# Example:
# Input:"-1/2+1/2+1/3"
# Output: "1/3"


import re
class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def str2fraction(s):
            num, den = s.split('/')
            return (int(num), int(den))
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        fracs = []
        pos = 0
        for i in range(len(expression)):
            if expression[i] in '+-' and i:
                fracs.append(str2fraction(expression[pos: i]))
                pos = i
        fracs.append(str2fraction(expression[pos:]))
        num, den = 0, 1
        for n, d in fracs:
            if den % d == 0 and d != 1:
                num += n * (den / d)
            else:
                num = num * d + n * den
                den = den * d
        g = gcd(max(abs(den), abs(num)), min(abs(den), abs(num)))
        return "%d/%d" % (num/g, den/g)