class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1 # 0 elements used, current sum is 0 -> 1 way

        for i in range(len(nums)):
            nextDP = defaultdict(int)
            for cur_sum, count in dp.items():
                nextDP[cur_sum + nums[i]] += count
                nextDP[cur_sum - nums[i]] += count
                dp = nextDP
        
        return dp[target]
