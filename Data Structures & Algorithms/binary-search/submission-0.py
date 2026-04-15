class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + (r - l)) // 2
        while l <= r:
            if target > nums[mid]:
                l = mid + 1
                mid = (l + r) // 2
            elif target < nums[mid]:
                r = mid - 1
                mid = (l + r) // 2
            if target == nums[mid]:
                return mid
        return -1