
class Solution:
    def heapify(self, nums, ind, val):
        n = len(nums)
        nums[ind] = val

        parent = (ind - 1) // 2

        if ind > 0 and nums[ind] < nums[parent]:
            while ind > 0:
                parent = (ind - 1) // 2

                if nums[ind] < nums[parent]:
                    nums[ind], nums[parent] = nums[parent], nums[ind]
                    ind = parent
                else:
                    break
        else:
            while True:
                smallest = ind
                left = 2 * ind + 1
                right = 2 * ind + 2

                if left < n and nums[left] < nums[smallest]:
                    smallest = left

                if right < n and nums[right] < nums[smallest]:
                    smallest = right

                if smallest == ind:
                    break

                nums[ind], nums[smallest] = nums[smallest], nums[ind]
                ind = smallest

        return nums

