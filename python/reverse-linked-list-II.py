# Time complexity O(n)
# Space complexity O(1)
def reverseBetween(head, left, right):
    if not head:
        return None

    prev, curr = None, head
    while left > 1:
        prev, curr = curr, curr.next
        left, right = left - 1, right - 1

    start, end = prev, curr
    while right:
        curr.next, prev, curr = prev, curr, curr.next
        right -= 1

    if start:
        start.next = prev
    else:
        head = prev
    end.next = curr
    return head
