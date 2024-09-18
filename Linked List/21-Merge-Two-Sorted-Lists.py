# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        # Traverse both lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If there are remaining nodes in list1, append them
        if list1:
            current.next = list1

        # If there are remaining nodes in list2, append them
        if list2:
            current.next = list2

        # Return the merged list, starting from the next node after dummy
        return dummy.next
        