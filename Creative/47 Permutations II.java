// Url: https://leetcode.com/problems/permutations-ii/
// Related Topics:
// Array Backtracking

// Example 1:
// Input: nums = [1,1,2]
// Output:
// [[1,1,2],
//  [1,2,1],
//  [2,1,1]]

// Example 2:
// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

// Creative 
// Backtracking

class Solution {
    private boolean[] visit;
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<Integer> arr = new ArrayList<>();
        Arrays.sort(nums);
        visit = new boolean[nums.length];
        List<List<Integer>> results = new ArrayList<>();
        backtrack(nums, results, arr, 0);
        return results;
    }

    public void backtrack(int[] nums, List<List<Integer>> results, List<Integer> arr, int pos) {
        if (nums.length == pos) {
            results.add(new ArrayList<>(arr));
        }
        for (int i = 0; i < nums.length; i++) {
            if (visit[i] || i > 0 && nums[i] == nums[i-1] && !visit[i-1])
                continue;
            arr.add(nums[i]);
            visit[i] = true;
            backtrack(nums, results, arr, pos + 1);
            visit[i] = false;
            arr.remove(pos);
        }
    }
}