"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_copy = {}
        if not head:
            return None
        curr = head
        while curr:
            new_copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = new_copy[curr]
            copy.next = new_copy.get(curr.next)
            copy.random = new_copy.get(curr.random)
            curr = curr.next
        return new_copy[head]