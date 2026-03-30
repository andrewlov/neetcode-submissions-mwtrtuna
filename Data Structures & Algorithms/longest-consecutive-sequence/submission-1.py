class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        subsequences = defaultdict(list)
        for num in nums:
            if num - 1 in numSet:
                continue
            subsequences[num] = [num]
            target = num + 1
            while target in numSet:
                subsequences[num].append(target)
                target += 1

        longestLength = 0
        for key in subsequences:
            subsequence = subsequences[key]
            if len(subsequence) > longestLength:
                longestLength = len(subsequence)
        return longestLength
