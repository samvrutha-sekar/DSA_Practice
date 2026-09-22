class Solution:
    def findPeakGrid(self, mat):
        m = len(mat)
        n = len(mat[0])

        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            max_row = 0

            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            left = mat[max_row][mid - 1] if mid > 0 else -1
            right = mat[max_row][mid + 1] if mid < n - 1 else -1

            if mat[max_row][mid] > left and mat[max_row][mid] > right:
                return [max_row, mid]

            elif right > mat[max_row][mid]:
                low = mid + 1

            else:
                high = mid - 1

        return [-1, -1]
