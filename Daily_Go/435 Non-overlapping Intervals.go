// Url: https://leetcode.com/problems/non-overlapping-intervals/
// Related Topics:
// Array DP Greedy Sorting

// Example 1:
// Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
// Output: 1
// Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

// Example 2:
// Input: intervals = [[1,2],[1,2],[1,2]]
// Output: 2
// Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

// Example 3:
// Input: intervals = [[1,2],[2,3]]
// Output: 0
// Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

func eraseOverlapIntervals(intervals [][]int) int {
    n := len(intervals)
    if n == 0 || n == 1 {
        return 0
    }
    sort.Slice(intervals, func (i, j int) bool {return intervals[i][1] < intervals[j][1]})
    cnt, right := 0, intervals[0][1]
    for i := 1; i < len(intervals); i++ {
        if intervals[i][0] < right {
            cnt++
        } else {
            right = intervals[i][1]
        }
    }
    return cnt
}