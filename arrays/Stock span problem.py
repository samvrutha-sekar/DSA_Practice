class Solution:
    def stockSpan(self, arr, n):
        span = [1] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            if stack:
                span[i] = i - stack[-1]
            else:
                span[i] = i + 1

            stack.append(i)

        return span