class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        count = {}

        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        left = 0
        required = len(t)
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            if s[right] in count:
                if count[s[right]] > 0:
                    required -= 1

                count[s[right]] -= 1

            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                if s[left] in count:
                    count[s[left]] += 1

                    if count[s[left]] > 0:
                        required += 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]