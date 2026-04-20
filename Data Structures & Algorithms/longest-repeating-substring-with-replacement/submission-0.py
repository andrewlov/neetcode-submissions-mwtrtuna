class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        maxSubstring = 0
        mode = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            mode = max(mode, hashmap[s[r]])

            while (r - l + 1) - mode > k:
                hashmap[s[l]] -= 1
                l += 1
            maxSubstring = max(maxSubstring, r - l + 1)

        return maxSubstring