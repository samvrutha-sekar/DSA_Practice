class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        second_largest = None

        for i in range(1, len(nums)):
            if nums[i] > largest:
                second_largest = largest
                largest = nums[i]
            elif nums[i] != largest and (second_largest is None or nums[i] > second_largest):
                second_largest = nums[i]

        if second_largest is None:
            return -1

        return second_largest