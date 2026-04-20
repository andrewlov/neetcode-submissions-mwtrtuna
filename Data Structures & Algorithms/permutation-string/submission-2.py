class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hash1 = {}
        for char in s1:
            hash1[char] = 1 + hash1.get(char, 0)

        matchesNeeded = len(hash1)
        for i in range(len(s2)):
            hash2 = {}
            currentMatches = 0
            for j in range(i, len(s2)):
                hash2[s2[j]] = 1 + hash2.get(s2[j], 0)
                if hash1.get(s2[j], 0) < hash2[s2[j]]:
                    break
                if hash1.get(s2[j], 0) == hash2[s2[j]]:
                    currentMatches += 1
                if currentMatches == matchesNeeded:
                    return True
        return False

            