class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS - children are 0 to j 
        res = 0
        l = r = 0 # our window for the current level
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            res += 1
        return res