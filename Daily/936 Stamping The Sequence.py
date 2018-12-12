# Url: https://leetcode.com/problems/stamping-the-sequence/
# Related Topics:
# String Greedy

# Example:
# Input: stamp = "abc", target = "ababc"
# Output: [0,2]


from collections import deque
class Solution:
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        if stamp not in target or len(stamp) > len(target) or len(set(stamp)) != len(set(target)):
            return []
        stamp_list = deque([stamp])
        l = len(stamp)
        for i in range(l-1, 0, -1):
            for start in range(l - i + 1):
                pattern = ['?'] * l
                pattern[start:start+i] = stamp[start:start+i]
                stamp_list.append(''.join(pattern))
        i, max_step = 0, 10 * len(target) + 1
        ans = []
        while max_step:
            flag, max_try = -1, len(stamp_list)
            while flag < 0 and max_try:
                flag = target.find(stamp_list[0])
                if flag < 0:
                    max_try -= 1
                    stamp_list.append(stamp_list.popleft())
            if flag >= 0:
                target = target[:flag] + '?'*l + target[flag+l:]
                ans.append(flag)
                max_step -= 1
            else:
                break
        if set(target) == set('?'):
            return ans[::-1]
        return []