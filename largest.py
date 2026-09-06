class Solution:
    def largestElement(self, nums):
        largest = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]

        return largest
    