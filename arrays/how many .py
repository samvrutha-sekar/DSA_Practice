class Solution:
    def countOccurrences(self, nums, target):
        first = self.findFirst(nums, target)

        if first == -1:
            return 0

        last = self.findLast(nums, target)

        return last - first + 1

    def findFirst(self, nums, target):
        low = 0
        high = len(nums) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                ans = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return ans

    def findLast(self, nums, target):
        low = 0
        high = len(nums) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                ans = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return ans
