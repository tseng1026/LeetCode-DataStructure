# https://leetcode.com/problems/longest-happy-string/

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(heap)

        result = ""
        while heap and heap[0][0] != 0:
            count, letter = heapq.heappop(heap)

            if len(result) >= 2 and letter == result[-1] == result[-2]:
                if heap and heap[0][0] != 0:
                    next_count, next_letter = heapq.heappop(heap)
                    result += next_letter
                    heapq.heappush(heap, (count, letter))
                    heapq.heappush(heap, (next_count + 1, next_letter))

                else:
                    return result

            else:
                result += letter
                heapq.heappush(heap, (count + 1, letter))

        return result
