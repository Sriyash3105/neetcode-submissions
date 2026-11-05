# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        times = count // k
        remaining = count % k
        if times == 0:
            return head
        curr = head
        new_head = None
        tail = None
        while times:
            count = k
            prev = None
            group_tail = curr
            while count:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count -= 1
            if new_head is None:
                new_head = prev
            else:
                tail.next = prev
            tail = group_tail
            times -= 1
        tail.next = curr
        return new_head