# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totalNodes = 0
        current = head
        while current:
            current = current.next
            totalNodes += 1
        nodeToDelete = totalNodes - n
        if nodeToDelete == 0:
            return head.next # would be the rest of the list or an empty list if it a size of list 1
        
        current = head
        i = 0
        while True:
            if (i + 1) == nodeToDelete:
                current.next = current.next.next
                break
            i += 1
            current = current.next
        return head
            