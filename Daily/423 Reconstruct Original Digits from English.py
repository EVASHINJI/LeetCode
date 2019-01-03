# Url: https://leetcode.com/problems/reconstruct-original-digits-from-english/
# Related Topics:
# Math

# Example:
# Input: "owoztneoer"
# Output: "012"


class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def update(cnt, letters, unique, num):
            times = cnt[ord(unique) - ord('a')]
            nums = [num] * times
            for c in letters:
                cnt[ord(c) - ord('a')] -= times
            return nums
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        ans = []
        ans.extend(update(cnt, 'zero', 'z', '0'))
        ans.extend(update(cnt, 'two', 'w', '2'))
        ans.extend(update(cnt, 'six', 'x', '6'))
        ans.extend(update(cnt, 'eight', 'g', '8'))
        ans.extend(update(cnt, 'seven', 's', '7'))
        ans.extend(update(cnt, 'three', 't', '3'))
        ans.extend(update(cnt, 'four', 'r', '4'))
        ans.extend(update(cnt, 'five', 'f', '5'))
        ans.extend(update(cnt, 'nine', 'i', '9'))
        ans.extend(update(cnt, 'one', 'o', '1'))
        ans.sort()
        return ''.join(ans)
