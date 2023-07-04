# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr_temp = head
        curr_temp1 = head
        length = 0
        while curr_temp:
            length += 1
            curr_temp = curr_temp.next
        remain_len = length - n
        count = 1
        if length - n == 0:
            return head.next
        while curr_temp1:

            if count == remain_len:
                curr_temp1.next = curr_temp1.next.next

            else:
                print(curr_temp1.val)
                curr_temp1 = curr_temp1.next
            count += 1

        return head
