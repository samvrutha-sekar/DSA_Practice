class Solution:
    def findMedian(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        low = min(row[0] for row in matrix)
        high = max(row[-1] for row in matrix)

        while low <= high:
            mid = (low + high) // 2

            count = 0

            for row in matrix:
                left = 0
                right = n - 1

                while left <= right:
                    middle = (left + right) // 2

                    if row[middle] <= mid:
                        left = middle + 1
                    else:
                        right = middle - 1

                count += left

            if count <= (m * n) // 2:
                low = mid + 1
            else:
                high = mid - 1

        return low
