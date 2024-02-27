# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        linked_list_l, linked_list_r = ListNode(), ListNode()
        left_node, right_node = linked_list_l, linked_list_r

        while head:
            if x > head.val:
                left_node.next = head
                left_node = left_node.next
            elif x <= head.val:
                right_node.next = head
                right_node = right_node.next
            head = head.next
        right_node.next = None
        left_node.next = linked_list_r.next

        return linked_list_l.next