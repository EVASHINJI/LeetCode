# Url: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Related Topics:
# String HashTable TwoPointers

# Example:
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]


from collections import Counter
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not len(words) or not len(words[0]) or not len(s):
            return []
        num, l = len(words), len(words[0])
        target = Counter(words)
        w2i = {w: i for i, w in enumerate(target.keys())}
        ans = []
        for i in range(len(s)-l*num+1):
            cur = s[i: i+l]
            if cur in w2i:
                seen = [0] * num
                seen[w2i[cur]] = 1
                for j in range(i + l, i + num * l, l):
                    w = s[j: j+l]
                    if w in w2i and seen[w2i[w]] != target[w]:
                        seen[w2i[w]] += 1
                    else:
                        break
                else:
                    ans.append(i)
        return ans