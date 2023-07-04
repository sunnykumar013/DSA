# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Geeks Solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr_node = head
        while curr_node and curr_node.next:
            if curr_node.val != curr_node.next.val:
                curr_node.val, curr_node.next.val = curr_node.next.val, curr_node.val

            curr_node = curr_node.next.next

        return head
