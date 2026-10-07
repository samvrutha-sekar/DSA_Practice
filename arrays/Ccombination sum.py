class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def backtrack(start, target, path):
            if target == 0:
                ans.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return ans