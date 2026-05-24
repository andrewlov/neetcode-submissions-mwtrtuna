class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, flag):
            if i == len(nums) - 1:
                return max(0, nums[i]) if flag else nums[i]
            if (i, flag) in cache:
                return cache[(i, flag)]

            if flag:
                cache[(i, flag)] = max(0, nums[i] + dfs(i + 1, True))
            else:
                cache[(i, flag)] = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
            
            return cache[(i, flag)]
        return dfs(0, False)