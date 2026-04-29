class MedianFinder:

    def __init__(self):
        self.small = [] # maxHeap
        self.large = [] # minHeap

    def addNum(self, num: int) -> None:
        # add it to either the small heap or the large heap
        # balance it if the difference in length of whatever it got added to is greater than 1
        # pop from one and push to the other
        heapq.heappush(self.small, -1 * num)

        # make sure every element in small is <= every element in large
        if (self.small and self.large and (-1 * self.small[0] > self.large[0])):
            val = -1. * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # make sure that the size is at most 1
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        