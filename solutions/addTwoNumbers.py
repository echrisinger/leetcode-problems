# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        
        total = (l1.val + l2.val)
        head = ListNode(total % 10)
        carry = total // 10
        l1 = l1.next
        l2 = l2.next
        curr = head
        
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
                
            curr.next = ListNode(total % 10)
            curr = curr.next
            carry = total // 10

        return head

