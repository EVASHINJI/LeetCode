# Url: https://leetcode.com/problems/group-anagrams/
# Related Topics:
# String HashTable

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def count(word):
            cnt = [0] * 26
            for c in word:
                cnt[ord(c) - ord('a')] += 1
            return tuple(cnt)
        
        group = defaultdict(list)
        for word in strs:
            group[count(word)].append(word)
        
        return [grp for grp in group.values()]