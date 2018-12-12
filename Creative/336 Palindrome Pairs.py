# Url: https://leetcode.com/problems/palindrome-pairs/
# Related Topics:
# String HashTable Trie

# Example:
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]] 

# Creative 
# similar to shortest palindrome find the common palindrome substring
# shouldn't consider too much details to enumerate the candidate


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        cache, lens = {}, set()
        for i, w in enumerate(words):
            cache[w] = i
            lens.add(len(w))
        lens = sorted(lens)
        
        ans = []
        for i in range(len(words)):
            word_i = words[i]
            word_r = word_i[::-1]
            word_len = len(word_i)
            if word_r in cache and cache[word_r] > i:
                ans.append([i, cache[word_r]])
                ans.append([cache[word_r], i])
            for l in lens:
                if l >= word_len:
                    break
                # common
                prefix = word_r[:l]
                suffix = word_r[word_len-l:]
                if prefix in cache and word_r[l:] == word_i[:word_len - l]:
                    ans.append([cache[prefix], i])
                if suffix in cache and word_r[:word_len - l] == word_i[l:]:
                    ans.append([i, cache[suffix]])
        return ans
