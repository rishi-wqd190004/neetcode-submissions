class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans, res = [], 0
        for op in operations:
            if op == "+":
                res += ans[-1] + ans[-2]
                ans.append(ans[-1]+ ans[-2])
            elif op == "D":
                res += (2 * ans[-1])
                ans.append(2*ans[-1])
            elif op == "C":
                res -= ans.pop()
            else:
                res += int(op)
                ans.append(int(op))
        return res