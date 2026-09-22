class Solution:
    def countPrefixOccurrences(self, s: str):
        n = len(s)

        lps = [0] * n

        for i in range(1, n):
            j = lps[i - 1]

            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]

            if s[i] == s[j]:
                j += 1

            lps[i] = j

        count = [0] * (n + 1)

        for i in range(n):
            count[lps[i]] += 1

        for i in range(n, 0, -1):
            count[lps[i - 1]] += count[i]

        for i in range(1, n + 1):
            count[i] += 1

        return count[1:]
