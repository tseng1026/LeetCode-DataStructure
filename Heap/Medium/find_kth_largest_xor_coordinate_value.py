# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    pass

                elif i == 0:
                    matrix[i][j] = matrix[i][j - 1] ^ matrix[i][j]

                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j] ^ matrix[i][j]

                else:
                    matrix[i][j] = matrix[i - 1][j - 1] ^ \
                        matrix[i - 1][j] ^ \
                        matrix[i][j - 1] ^ \
                        matrix[i][j]

                heapq.heappush(heap, matrix[i][j])

                if len(heap) > k:
                    heapq.heappop(heap)

        return heap[0]
