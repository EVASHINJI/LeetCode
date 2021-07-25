// Url: https://leetcode.com/problems/baseball-game/
// Related Topics:
// Array Stack Simulation

// Example 1:
// Input: ops = ["5","2","C","D","+"]
// Output: 30
// Explanation:
// "5" - Add 5 to the record, record is now [5].
// "2" - Add 2 to the record, record is now [5, 2].
// "C" - Invalidate and remove the previous score, record is now [5].
// "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
// "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
// The total sum is 5 + 10 + 15 = 30.

// Example 2:
// Input: ops = ["5","-2","4","C","D","9","+","+"]
// Output: 27
// Explanation:
// "5" - Add 5 to the record, record is now [5].
// "-2" - Add -2 to the record, record is now [5, -2].
// "4" - Add 4 to the record, record is now [5, -2, 4].
// "C" - Invalidate and remove the previous score, record is now [5, -2].
// "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
// "9" - Add 9 to the record, record is now [5, -2, -4, 9].
// "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
// "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
// The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

// Example 3:
// Input: ops = ["1"]
// Output: 1

class Solution {
    public int calPoints(String[] ops) {
        ArrayList<Integer> scoreList = new ArrayList<>();
        for (String op: ops) {
            int l = scoreList.size();
            switch (op) {
                case "+":
                    scoreList.add(scoreList.get(l - 1) + scoreList.get(l - 2));
                    break;
                case "C":
                    scoreList.remove(l - 1);
                    break;
                case "D":
                    scoreList.add(scoreList.get(l - 1) * 2);
                    break;
                default:
                    scoreList.add(Integer.valueOf(op));
            }
        }
        return scoreList.stream().reduce(0, (a, b) -> a + b);
    }
}