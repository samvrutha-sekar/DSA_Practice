class Solution:
    def leaders(self, nums):
        leaders = []
        max_right = nums[-1]

        leaders.append(max_right)

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_right:
                leaders.append(nums[i])
                max_right = nums[i]

        leaders.reverse()

        return leaders
        