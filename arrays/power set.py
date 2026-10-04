class Solution:
    def powerSet(self, nums):
        ans = []

        def backtrack(index, current):
            if index == len(nums):
                ans.append(current[:])
                return

            # Include the current element
            current.append(nums[index])
            backtrack(index + 1, current)

            # Exclude the current element
            current.pop()
            backtrack(index + 1, current)

        backtrack(0, [])
        return ans