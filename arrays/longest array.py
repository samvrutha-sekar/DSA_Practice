class Solution:
    def longestSubarray(self, nums, k):
        left = 0
        total = 0
        maximum = 0

        for right in range(len(nums)):
            total += nums[right]

            while total > k and left <= right:
                total -= nums[left]
                left += 1

            if total == k:
                maximum = max(maximum, right - left + 1)

        return maximum
