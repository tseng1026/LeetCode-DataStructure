# https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [(-count, 1) for _, count in counter.items()]
        heapq.heapify(heap)

        result = 0
        while heap:
            result += 1

            for idx, (count, timestamp) in enumerate(heap):
                if result >= timestamp:
                    negcount = -(-count - 1) if -count - 1 else -float("inf")
                    heap[idx] = (negcount, result + n + 1)
                    heapq.heapify(heap)
                    break

            if heap[0][0] == -float("inf"):
                heapq.heappop(heap)

        return result
