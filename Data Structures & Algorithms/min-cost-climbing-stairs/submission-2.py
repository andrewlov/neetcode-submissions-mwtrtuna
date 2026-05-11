class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hashmap = {}

        def dfs(i):
            if i >= len(cost):
                return 0 
            if i in hashmap:
                return hashmap[i]
            cost[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            hashmap[i] = cost[i]
            return cost[i]
        return min(dfs(0), dfs(1))