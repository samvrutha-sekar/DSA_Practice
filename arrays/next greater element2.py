class Solution:
    def nextGreaterElements(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            idx = i % n

            while stack and stack[-1] <= arr[idx]:
                stack.pop()

            if i < n and stack:
                result[idx] = stack[-1]

            stack.append(arr[idx])

        return result