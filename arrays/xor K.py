class Solution:
    def subarraysWithXorK(self, nums, k):
        xor_value = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            xor_value ^= num

            required = xor_value ^ k

            if required in freq:
                count += freq[required]

            freq[xor_value] = freq.get(xor_value, 0) + 1

        return count
