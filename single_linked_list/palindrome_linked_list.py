class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nextnode = slow.next
            slow.next = prev
            prev = slow
            slow = nextnode
        
        while prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next

        return True
