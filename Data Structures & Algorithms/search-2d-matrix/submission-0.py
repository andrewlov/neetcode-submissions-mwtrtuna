class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        mid = (i + j) // 2
        row = 0
        while i <= j:
            if target > matrix[mid][-1]:
                i = mid + 1
                mid = (i + j) // 2
            elif target < matrix[mid][0]:
                j = mid - 1
                mid = (i + j) // 2
            else:
                row = mid
                break
        if not (i <= j):
            return False

        l, r = 0, len(matrix[row]) - 1
        mid2 = (l + r) // 2
        while l <= r:
            if target > matrix[row][mid2]:
                l = mid2 + 1
                mid2 = (l + r) // 2
            elif target < matrix[row][mid2]:
                r = mid2 - 1
                mid2 = (l + r) // 2
            else:
                return True
        return False