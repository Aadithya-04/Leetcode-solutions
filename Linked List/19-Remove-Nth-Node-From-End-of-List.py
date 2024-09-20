# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            dummy = ListNode(0, head)
            slow = dummy
            fast = head

        # Move fast n steps ahead
            for _ in range(n):
                if fast:
                    fast = fast.next

        # Move both pointers until fast reaches the end
            while fast:
                slow = slow.next
                fast = fast.next

        # Remove the nth node from the end
            slow.next = slow.next.next  # Correctly link the previous node to the node after the one being removed

            return dummy.next  # Return the new head
        