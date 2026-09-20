class Solution:
    def maxTwo(self, nums1, nums2):
        first = float("-inf")
        second = float("-inf")

        for num in nums1 + nums2:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num

        return first, second
