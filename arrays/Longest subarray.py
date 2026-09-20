class Solution:
    def longestSubarray(self, nums, k):
        prefix_sum = 0
        maximum = 0
        first = {0: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in first:
                maximum = max(maximum, i - first[prefix_sum - k])

            if prefix_sum not in first:
                first[prefix_sum] = i

        return maximum
