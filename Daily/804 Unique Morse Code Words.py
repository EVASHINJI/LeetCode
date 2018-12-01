# Url: https://leetcode.com/problems/unique-morse-code-words/
# Related Topics:
# String

# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        encode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in words:
            code = ''.join([encode[ord(c) - ord('a')] for c in word])
            seen.add(code)
        return len(seen)