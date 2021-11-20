// Url: https://leetcode.com/problems/beautiful-arrangement/
// Related Topics:
// Array BitManipulation DP Backtracking BitMask

// Example 1:
// Input: n = 2
// Output: 2
// Explanation: 
// The first beautiful arrangement is [1,2]:
//     - perm[1] = 1 is divisible by i = 1
//     - perm[2] = 2 is divisible by i = 2
// The second beautiful arrangement is [2,1]:
//     - perm[1] = 2 is divisible by i = 1
//     - i = 2 is divisible by perm[2] = 1

// Example 2:
// Input: n = 1
// Output: 1

// Creative 
// Solution1: use matched to enum every possible val in pos-i, not iterate the whole val
// Solution2: BitCounter to record current valid pos num, BitMask to record the val be used. 
// and f[mask ^ (1 << i)] calculate before f[mask], so f[mask] can be accumulated by f[mask - (1 << i)] 

class Solution1 {
    List<Integer>[] matched;
    boolean[] vis;
    int num;

    public void backtrack(int index, int n) {
        if (index == n + 1) {
            num += 1;
            return;
        }
        for (Integer x : matched[index]) {
            if (!vis[x]) {
                vis[x] = true;
                backtrack(index+1, n);
                vis[x] = false;
            }
        }
    }

    public int countArrangement(int n) {
        vis = new boolean[n + 1];
        matched = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            matched[i] = new ArrayList<>();
            for (int j = 1; j <= n; j++) {
                if (i % j == 0 || j % i == 0) {
                    matched[i].add(j);
                }
            }
        }
        backtrack(1, n);
        return num;
    }
}

class Solution2 {
    public int countArrangement(int n) {
        int[] f = new int[1 << n];
        f[0] = 1;
        for (int mask = 1; mask < 1 << n; mask++) {
            int num = Integer.bitCount(mask);
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0 && (num % (i+1) == 0 || (i+1) % num == 0)) {
                    f[mask] += f[mask ^ (1 << i)];
                }
            }
        }
        return f[(1 << n) - 1];
    }
}