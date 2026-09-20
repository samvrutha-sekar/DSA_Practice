class Solution:
    def upperBound(self, nums, x):
        low = 0
        high = len(nums) - 1
        ans = len(nums)

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
