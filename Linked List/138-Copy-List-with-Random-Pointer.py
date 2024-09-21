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
        if not head:
            return None
        
        # Step 1: Create new nodes and interleave them with original nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers for the new nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the two lists
        curr = head
        new_head = head.next
        copy_curr = new_head
        
        while curr:
            curr.next = curr.next.next  # Restore the original list
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next  # Link the copied list
            curr = curr.next
            copy_curr = copy_curr.next
        
        return new_head
        