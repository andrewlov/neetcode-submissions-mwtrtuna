class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        result = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                result += max(leftMax - height[l], 0)
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                result += max(rightMax - height[r], 0)
                rightMax = max(rightMax, height[r])
        return result