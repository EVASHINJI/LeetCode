// Url: https://leetcode.com/problems/relative-ranks/
// Related Topics:
// Array Sorting Heap

// Example 1:
// Input: score = [5,4,3,2,1]
// Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
// Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

// Example 2:
// Input: score = [10,3,8,9,4]
// Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
// Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

class Solution {
    public final static List<String> RANK_MEDAL = Arrays.asList("Gold Medal", "Silver Medal", "Bronze Medal");

    public String[] findRelativeRanks(int[] score) {
        List<Integer> scoreList = Arrays.stream(score).boxed().collect(Collectors.toList());
        scoreList.sort((n1, n2) -> n2 - n1);
        Map<Integer, String> rankMap = new HashMap<>();
        for (int i = 0; i < scoreList.size(); i++) {
            if (i < RANK_MEDAL.size()) {
                rankMap.put(scoreList.get(i), RANK_MEDAL.get(i));
            } else {
                rankMap.put(scoreList.get(i), (i + 1) + "");
            }

        }
        String[] ans = new String[score.length];
        for (int i = 0; i < score.length; i++) {
            ans[i] = rankMap.get(score[i]);
        }
        return ans;
    }
}