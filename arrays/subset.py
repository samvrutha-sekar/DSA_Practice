
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        arr = []

        def backtrack(ind):
            ans.append(arr.copy())

            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i - 1]:
                    continue

                arr.append(nums[i])
                backtrack(i + 1)
                arr.pop()

        backtrack(0)
        return ans
