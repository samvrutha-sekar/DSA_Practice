class Solution:
    def numberOfOddSubarrays(self, nums, k):
        def atMost(k):
            left = 0
            odd_count = 0
            ans = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1

                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)