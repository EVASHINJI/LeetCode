// Url: https://leetcode.com/problems/single-number-ii/
// Related Topics:
// Array BitManipulation

// Example 1:
// Input: nums = [2,2,3,2]
// Output: 3

// Example 2:
// Input: nums = [0,1,0,1,0,1,99]
// Output: 99

// Creative 
// when one constant cannot statisfy xor to record, 
// then use two and design a state machine

class Solution {
    public int singleNumber(int[] nums) {
        int one = 0, two = 0;
        for (int num : nums) {
            one = one ^ num & ~two;
            two = two ^ num & ~one;
        }
        return one;
    }
}