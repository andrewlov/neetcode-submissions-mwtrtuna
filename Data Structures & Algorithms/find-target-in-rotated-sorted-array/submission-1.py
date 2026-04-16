class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        pivot = l

        l, r = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1