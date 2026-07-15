from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}

        have = 0
        needCount = len(need)

        left = 0
        result = [-1, -1]
        minLength = float("inf")

        for right in range(len(s)):

            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == needCount:

                if (right - left + 1) < minLength:
                    minLength = right - left + 1
                    result = [left, right]

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        left, right = result

        if minLength == float("inf"):
            return ""

        return s[left:right + 1]
