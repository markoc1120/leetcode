class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity O(n)
# Space complexity O(1)
def deleteDuplicates(head):
    dummy = ListNode(0, head)
    curr, prev = head, dummy
    while curr:
        while curr.next and curr.val == curr.next.val:
            curr = curr.next

        if prev.next == curr:
            prev, curr = prev.next, curr.next
        else:
            prev.next, curr = curr.next, prev.next
    return dummy.next
