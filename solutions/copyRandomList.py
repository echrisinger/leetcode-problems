"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        nodes = {}
        curr = head
        prev = None
        while curr:
            nodes[curr] = Node(curr.val)
            if prev:
                nodes[prev].next = nodes[curr]
            
            prev = curr
            curr = curr.next
        
        curr = head
        while curr:
            if curr.random:
                nodes[curr].random = nodes[curr.random]
            curr = curr.next
        
        return nodes[head]
        
# O(n) time, space - O(1) space ignoring return type
