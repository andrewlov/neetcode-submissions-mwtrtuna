class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        totalLength = len(A) + len(B)
        l, r = 0, len(A) - 1
        while True:
            midA = (l + r) // 2
            midB = totalLength // 2 - midA - 2
            
            Aleft = A[midA] if midA >= 0 else float("-infinity")
            Aright = A[midA + 1] if (midA + 1) < len(A) else float("infinity")
            Bleft = B[midB] if midB >= 0 else float("-infinity")
            Bright = B[midB + 1] if (midB + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if totalLength % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1
            