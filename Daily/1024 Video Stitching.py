# Url: https://leetcode.com/problems/video-stitching/
# Related Topics:
# DP

# Example 1:
# Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
# Output: 3
# Explanation: 
# We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
# Then, we can reconstruct the sporting event as follows:
# We cut [1,9] into segments [1,2] + [2,8] + [8,9].
# Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

# Example 2:
# Input: clips = [[0,1],[1,2]], T = 5
# Output: -1
# Explanation: 
# We can't cover [0,5] with only [0,1] and [0,2].


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        ans, cur_end, cand_end = 0, 0, 0
        for start, end in sorted(clips) + [[float('inf'), float('inf')]]:
            if start > cur_end:
                cur_end = cand_end
                ans += 1
                if cur_end >= T:
                    break
            if start <= cur_end:
                cand_end = max(cand_end, end)
                
        return ans if cur_end >= T else -1