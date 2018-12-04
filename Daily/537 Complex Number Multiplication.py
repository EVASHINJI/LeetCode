# Url: https://leetcode.com/problems/complex-number-multiplication/
# Related Topics:
# String Math

# Example:
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"


class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def read_complex(c):
            real, image = c.split('+')
            return int(real), int(image[:-1])
        r1, i1 = read_complex(a)
        r2, i2 = read_complex(b)
        ans_r, ans_i = r1*r2 - i1*i2, r1*i2 + r2*i1
        return '%d+%di' % (ans_r, ans_i)