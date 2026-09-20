class Solution:
    def minimumRateToEatBananas(self, nums, h):
        low = 1
        high = max(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            hours = 0

            for bananas in nums:
                hours += (bananas + mid - 1) // mid

            if hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
