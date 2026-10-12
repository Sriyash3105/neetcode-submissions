# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        reversed_head = reverse(head)
        
        if n == 1:
            reversed_head = reversed_head.next
        else:
            curr = reversed_head
            for _ in range(n - 2):
                curr = curr.next
            curr.next = curr.next.next
            
        return reverse(reversed_head)
        