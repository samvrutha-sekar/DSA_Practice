class Solution:
    def generateRow(self, n):
        row = [1]
        ans = 1

        for i in range(1, n):
            ans = ans * (n - i) // i
            row.append(ans)

        return row
