class Solution:
    def aggressiveCows(self, nums, k):
        nums.sort()

        low = 1
        high = nums[-1] - nums[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            count = 1
            last = nums[0]

            for i in range(1, len(nums)):
                if nums[i] - last >= mid:
                    count += 1
                    last = nums[i]

            if count >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans