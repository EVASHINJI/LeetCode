# Url: https://leetcode.com/problems/bulls-and-cows/
# Related Topics:
# HashTable

# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# Example 2:
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.


from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        digits = Counter(secret)
        bulls, cows = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
                digits[g] -= 1
        
        for s, g in zip(secret, guess):
            if s != g and g in digits and digits[g]:
                cows += 1
                digits[g] -= 1
                
        return '%dA%dB' % (bulls, cows)