# Time complexity O(n)
# Space complexity O(1)
def deleteMiddle(head):
    if not head or not head.next:
        return None

    prev, slow, fast, dummy = None, head, head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if slow.next:
        prev.next = slow.next
    else:
        dummy.next = None

    return dummy
