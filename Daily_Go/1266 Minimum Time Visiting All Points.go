// Url: https://leetcode.com/problems/minimum-time-visiting-all-points/
// Related Topics:
// Array Math Geometry

// Example 1:
// Input: points = [[1,1],[3,4],[-1,0]]
// Output: 7
// Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
// Time from [1,1] to [3,4] = 3 seconds 
// Time from [3,4] to [-1,0] = 4 seconds
// Total time = 7 seconds

// Example 2:
// Input: points = [[3,2],[-2,2]]
// Output: 5

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}

func minTimeToVisitAllPoints(points [][]int) int {
    if len(points) <= 1 {
        return 0
    }
    x0, y0 := points[0][0], points[0][1]
    sec := 0
    for i := 1; i < len(points); i++ {
        x1, y1 := points[i][0], points[i][1]
        dx, dy := x1 + x0 - 2*min(x1,x0), y1 + y0 - 2*min(y1,y0)
        sec += dx + dy - min(dx, dy)
        x0, y0 = x1, y1
    }
    return sec
}