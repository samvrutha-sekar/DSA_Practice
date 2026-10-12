
class Solution:
    def partition(self, s: str):
        ans = []
        arr = []

        def backtrack(ind):
            if ind == len(s):
                ans.append(arr.copy())
                return

            for i in range(ind, len(s)):
                sub = s[ind:i + 1]

                if sub == sub[::-1]:
                    arr.append(sub)
                    backtrack(i + 1)
                    arr.pop()

        backtrack(0)
        return ans
