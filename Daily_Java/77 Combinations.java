// Url: https://leetcode.com/problems/combinations/
// Related Topics:
// Array Backtracking

// Example 1:
// Input: n = 4, k = 2
// Output:
// [
//   [2,4],
//   [3,4],
//   [2,3],
//   [1,2],
//   [1,3],
//   [1,4],
// ]

// Example 2:
// Input: n = 1, k = 1
// Output: [[1]]

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), n, k);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> arr, int n, int k) {
        if (k == 0) {
            result.add(new ArrayList<>(arr));
            return;
        }

        int start = arr.size() == 0 ? 0 : arr.get(arr.size()-1);
        for (int i = start + 1; i <= n - k + 1; i++) {
            arr.add(i);
            backtrack(result, arr, n, k - 1);
            arr.remove(arr.size() - 1);
        }
    }
}