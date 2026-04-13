# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

        prevGroup = dummy

        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next

            # reverse the prevGroup
            prev, curr = nextGroup, prevGroup.next
            while curr != nextGroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp
        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
