# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count+=1
            curr = curr.next
        rem = count - n
        curr = head
        if rem == 0:
            return head.next
        for i in range(count-1):
            if (i+1) == rem:
                curr.next = curr.next.next
                break
            curr = curr.next 
        return head           
