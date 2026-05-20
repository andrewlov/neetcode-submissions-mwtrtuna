class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for total in dp:
                if total + nums[i] == target:
                    return True
                nextDP.add(total + nums[i])
                nextDP.add(total)
            dp = nextDP
        return True if target in dp else False