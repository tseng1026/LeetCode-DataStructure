# https://leetcode.com/problems/exclusive-time-of-functions/

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        START, END = "start", "end"

        result = defaultdict(int)
        stack = []
        for log in logs:
            idx, stamptype, timestamp = log.split(":")
            timestamp = int(timestamp)

            if stamptype == START:
                if stack:
                    stack[-1][3] = stack[-1][3] + timestamp - stack[-1][2]
                    stack[-1][2] = timestamp
                stack.append([idx, stamptype, timestamp, 0])

            else:
                timestamp += 1
                result[idx] += stack[-1][3] + timestamp - stack[-1][2]
                stack.pop()
                if stack:
                    stack[-1][2] = timestamp

        return [result[str(k)] for k in range(n)]
