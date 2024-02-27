class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listnode = prev = ListNode()
        listnode.next = head
        left, right = listnode, listnode.next
        while (n > 0 and right):
            right = right.next
            n -= 1
        
        while (right):
            left = left.next
            right = right.next

        left.next = left.next.next

        return listnode.next