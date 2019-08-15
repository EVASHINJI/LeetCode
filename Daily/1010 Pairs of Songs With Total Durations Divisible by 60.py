# Url: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# Related Topics:
# Array 

# Example 1:
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

# Example 2:
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = [0] * 60
        ans = 0
        for t in time:
            k1 = t % 60
            k2 = (60 - k1) % 60
            ans += cnt[k2]
            cnt[k1] += 1
        return ans
        