# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr_dummy = dummy
        curr_node = head
        count = 1
        while curr_node:
            if count % 2 != 0:
                new_node = ListNode(curr_node.val)
                print(new_node)
                curr_dummy.next = new_node
                curr_dummy = curr_dummy.next
                curr_node = curr_node.next
                count += 1
            else:
                curr_node = curr_node.next
                count += 1

        count = 1

        while head:
            if count % 2 == 0:
                new_node = ListNode(head.val)
                curr_dummy.next = new_node

                curr_dummy = curr_dummy.next
                head = head.next
                count += 1
            else:
                head = head.next
                count += 1

        return dummy.next





