class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        _set = set()
        curr = head
        _set.add(curr.val)
        while (curr.next):
            if curr.next.val in _set:
                curr.next = curr.next.next
            else:
                _set.add(curr.next.val)
                curr = curr.next
        return head