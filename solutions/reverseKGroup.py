# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        rev_head = rev_tail = None
        while head:
            curr_rev = curr_rev_tail = None
            curr_k = k
            while head and curr_k:
                tmp = head
                head = head.next
                tmp.next = curr_rev
                curr_rev = tmp
                if not curr_rev_tail:
                    curr_rev_tail = tmp
                
                curr_k -= 1
            
            if not rev_head:
                rev_head = curr_rev
            elif curr_k:
                rev_tail.next = self.reverse(curr_rev)
            else:
                rev_tail.next = curr_rev
            rev_tail = curr_rev_tail
        
        return rev_head
    
    def reverse(self, head):
        new_head = None
        while head:
            tmp = head
            head = head.next
            tmp.next = new_head
            new_head = tmp
            
        return new_head
            
            
# O(n), O(1)
