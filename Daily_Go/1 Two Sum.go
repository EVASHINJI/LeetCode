// Url: https://leetcode.com/problems/two-sum/
// Related Topics:
// Array HashTable

// Example 1:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Output: Because nums[0] + nums[1] == 9, we return [0, 1].

// Example 2:
// Input: nums = [3,2,4], target = 6
// Output: [1,2]

func twoSum(nums []int, target int) []int {
    dic := map[int]int{}
    for idx, n := range nums {
        last_idx, ok := dic[n]
        if ok {
            return []int{last_idx, idx}
        } else {
            dic[target - n] = idx
        }
    }
    return nil
}