// Url: https://leetcode.com/problems/sum-of-unique-elements/
// Related Topics:
// Array HashTable

// Example 1:
// Input: nums = [1,2,3,2]
// Output: 4
// Explanation: The unique elements are [1,3], and the sum is 4.

// Example 2:
// Input: nums = [1,1,1,1,1]
// Output: 0
// Explanation: There are no unique elements, and the sum is 0.

// Example 3:
// Input: nums = [1,2,3,4,5]
// Output: 15
// Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

class Solution {
    public int sumOfUnique(int[] nums) {
        HashMap<Integer, Integer> count = new HashMap<>();
        for (int n: nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }
        return count
            .entrySet()
            .stream()
            .filter(e -> e.getValue() < 2)
            .mapToInt(Map.Entry::getKey)
            .sum();
    }
}