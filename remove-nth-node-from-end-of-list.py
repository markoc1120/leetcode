class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity O(n)
# Space complexity O(1)
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    slow, fast = dummy, head
    while n:
        fast = fast.next
        n -= 1
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
