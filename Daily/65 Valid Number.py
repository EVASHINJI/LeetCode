# Url: https://leetcode.com/problems/valid-number/
# Related Topics:
# String Math

# Example:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        exp, sign, point, digit = True, True, True, False
        for c in s.strip():
            if c == 'e':
                if not digit or not exp:
                    return False
                else:
                    exp, sign, point, digit = False, True, False, False
                    continue
            elif c == '.':
                if not point:
                    return False
                point = False
            elif c == '+' or c == '-':
                if not sign:
                    return False
                sign = False
            elif c.isalpha():
                return False
            elif c.isdigit():
                digit = True
            else:
                return False
            sign = False
        return digit == True
                    
                    