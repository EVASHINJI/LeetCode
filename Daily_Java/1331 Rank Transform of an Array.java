// Url: https://leetcode.com/problems/rank-transform-of-an-array/
// Related Topics:
// Array HashTable Sorting

// Example 1:
// Input: arr = [40,10,20,30]
// Output: [4,1,2,3]
// Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

// Example 2:
// Input: arr = [100,100,100]
// Output: [1,1,1]
// Explanation: Same elements share the same rank.

// Example 3:
// Input: arr = [37,12,28,9,100,56,80,5,12]
// Output: [5,3,4,2,8,6,7,1,3]

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int[] sortArr = Arrays.copyOf(arr, arr.length);
        Arrays.sort(sortArr);
        int rank = 1;
        Map<Integer, Integer> rankMap = new HashMap<>();
        for (int i : sortArr) {
            if (rankMap.containsKey(i)) continue;
            rankMap.put(i, rank++);
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = rankMap.get(arr[i]);
        }
        return arr;
    }
}