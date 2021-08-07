// Url: https://leetcode.com/problems/permutations/
// Related Topics:
// Array Backtracking

// Example 1:
// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

// Example 2:
// Input: nums = [0,1]
// Output: [[0,1],[1,0]]

// Creative 
// Backtracking

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> arr = new ArrayList<>();
        for (int num : nums) {
            arr.add(num);
        }
        List<List<Integer>> results = new ArrayList<>();
        backtrack(results, arr, 0);
        return results;
    }

    public void backtrack(List<List<Integer>> results, List<Integer> arr, int pos) {
        if (arr.size() == pos) {
            results.add(new ArrayList<>(arr));
        }
        for (int i = pos; i < arr.size(); i++) {
            Collections.swap(arr, i, pos);
            backtrack(results, arr, pos + 1);
            Collections.swap(arr, i, pos);
        }
    }
}

class Solution {
    private boolean[] visit;
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> arr = new ArrayList<>();
        List<List<Integer>> results = new ArrayList<>();
        visit = new boolean[nums.length];
        backtrack(nums, results, arr, 0);
        return results;
    }

    public void backtrack(int[] nums, List<List<Integer>> results, List<Integer> arr, int pos) {
        if (nums.length == pos) {
            results.add(new ArrayList<>(arr));
        }
        for (int i = 0; i < nums.length; i++) {
            if (visit[i]) continue;
            arr.add(nums[i]);
            visit[i] = true;
            backtrack(nums, results, arr, pos + 1);
            visit[i] = false;
            arr.remove(pos);
        }
    }
}