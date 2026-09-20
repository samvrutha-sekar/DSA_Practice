class Solution:
    def roseGarden(self, n, nums, k, m):
        if m * k > n:
            return -1

        low = min(nums)
        high = max(nums)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            bouquets = 0
            flowers = 0

            for day in nums:
                if day <= mid:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
