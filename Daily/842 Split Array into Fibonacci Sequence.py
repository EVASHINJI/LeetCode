# Url: https://leetcode.com/problems/split-array-into-fibonacci-sequence/
# Related Topics:
# String BackTracking Greedy

# Example:
# Input: "1101111"
# Output: [110, 1, 111]


class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        for i in range(min(10, len(S) - 2)):
            first = int(S[:i+1])
            if first and S[0] == '0':
                break
            for j in range(1, min(10, len(S))):
                second = int(S[i+1: i+j+1])
                if second and S[i+1] == '0':
                    break
                fib = [first, second]
                k = i+j+1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
                    
        return []