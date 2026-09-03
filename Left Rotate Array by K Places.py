class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n

        nums[:] = nums[k:] + nums[:k]

        return nums