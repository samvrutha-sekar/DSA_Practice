class Solution:
    def majorityElement(self, nums):
        count1 = 0
        count2 = 0
        candidate1 = None
        candidate2 = None

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        ans = []

        for candidate in [candidate1, candidate2]:
            if candidate is not None and nums.count(candidate) > len(nums) // 3:
                if candidate not in ans:
                    ans.append(candidate)

        return ans
