from collections import defaultdict
class Solution:
    def tranversal(self, head):
        dict_t = defaultdict(int)
        curr = head
        while (curr):
            dict_t[curr.val] += 1
            curr = curr.next
        return dict_t

    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq = self.tranversal(head)
        listnode = prev = ListNode() 
        listnode.next = head

        curr = head
        while curr:
            if freq[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return listnode.next