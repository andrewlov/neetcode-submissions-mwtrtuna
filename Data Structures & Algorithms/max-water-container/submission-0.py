class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            if area > maxArea:
                maxArea = area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea