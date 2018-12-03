# Url: https://leetcode.com/problems/goat-latin/
# Related Topics:
# String

# Example:
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"


class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        goat_latin = []
        postfix = 'ma'
        for word in S.split(' '):
            postfix += 'a'
            if word[0].lower() in 'aeiou':
                goat_latin.append(word + postfix)
            else:
                goat_latin.append(word[1:] + word[0] + postfix)
        return ' '.join(goat_latin)