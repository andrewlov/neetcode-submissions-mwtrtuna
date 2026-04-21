class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, hasht = {}, {}

        for c in t:
            hasht[c] = 1 + hasht.get(c, 0)
        have, need = 0, len(hasht)
        res = [-1, -1]
        resLen = float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in hasht and window[c] == hasht[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in hasht and window[s[l]] < hasht[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""

