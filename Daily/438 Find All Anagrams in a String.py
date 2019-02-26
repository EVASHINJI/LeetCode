# Url: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Related Topics:
# HashTable

# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = Counter(p)
        usage = dict(p_cnt)
        ans = []
        l_s, l_p = len(s), len(p)
        lo, hi = 0, -1
        i = 0
        while i < l_s:
            if s[i] in usage:
                if usage[s[i]]:
                    usage[s[i]] -= 1
                    hi += 1
                    if hi - lo + 1 == l_p:
                        ans.append(lo)
                    i += 1
                else:
                    usage[s[lo]] += 1
                    lo += 1
            else:
                i += 1
                lo, hi = i, i - 1
                usage = dict(p_cnt)
        return ans