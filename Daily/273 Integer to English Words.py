# Url: https://leetcode.com/problems/integer-to-english-words/
# Related Topics:
# String Math

# Example:
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


class Solution:
    def __init__(self):
        self.less_than_20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]
        
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        
        res = ''
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + ' ' + res
                print(res)
            num = num // 1000
        return res.strip()
    
    def helper(self, num):
        if num == 0:
            return ''
        if num < 20:
            return self.less_than_20[num] + ' '
        if num < 100:
            return self.tens[num//10] + ' ' + self.helper(num%10)
        return self.less_than_20[num//100] + ' Hundred ' + self.helper(num % 100)