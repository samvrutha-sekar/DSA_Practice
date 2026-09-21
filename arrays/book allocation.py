class Solution:
    def findPages(self, nums, m):
        n = len(nums)

        if m > n:
            return -1

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            students = 1
            pages = 0

            for book in nums:
                if pages + book <= mid:
                    pages += book
                else:
                    students += 1
                    pages = book

            if students <= m:
                high = mid - 1
            else:
                low = mid + 1

        return low
