class Solution:
    def NthRoot(self, n, m):
        low = 1
        high = m

        while low <= high:
            mid = (low + high) // 2

            value = mid ** n

            if value == m:
                return mid
            elif value < m:
                low = mid + 1
            else:
                high = mid - 1

        return -1
