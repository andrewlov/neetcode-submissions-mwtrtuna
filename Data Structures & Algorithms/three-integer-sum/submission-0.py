class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, num in enumerate(nums):
            if index > 0 and nums[index - 1] == num: # if it is the same value/duplicate
                continue

            l, r = index + 1, len(nums) - 1

            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result