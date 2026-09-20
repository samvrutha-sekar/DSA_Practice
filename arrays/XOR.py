class Solution:
    def findMissing(self, nums):
        n = len(nums)
        xor_value = 0

        for i in range(n + 1):
            xor_value ^= i

        for num in nums:
            xor_value ^= num

        return xor_value
