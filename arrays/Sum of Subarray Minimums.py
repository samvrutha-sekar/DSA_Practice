class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        MOD = 10**9 + 7
        stack = []
        result = 0

        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()

                left = stack[-1] if stack else -1
                right = i

                count = (mid - left) * (right - mid)
                result = (result + arr[mid] * count) % MOD

            stack.append(i)

        return result