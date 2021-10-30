// Url: https://leetcode.com/problems/unique-number-of-occurrences/
// Related Topics:
// Array HashTable

// Example 1:
// Input: arr = [1,2,2,1,1,3]
// Output: true
// Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

// Example 2:
// Input: arr = [1,2]
// Output: false

func uniqueOccurrences(arr []int) bool {
    dic := map[int] int{}
    for _, a := range arr {
        dic[a]++
    }
    cnt_set := map[int] bool{}
    for _, cnt := range dic {
        if cnt_set[cnt] {
            return false
        } else {
            cnt_set[cnt] = true
        }
    }
    return true
}