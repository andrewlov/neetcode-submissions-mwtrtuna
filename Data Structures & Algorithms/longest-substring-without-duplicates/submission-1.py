class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0 
        currentLongest = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            currentLongest = max(currentLongest, len(seen))
        return currentLongest