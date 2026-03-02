class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity O(n)
# Space complexity O(1)
def reorderList(head: ListNode | None) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    mid, end = head, head
    while end and end.next:
        mid = mid.next
        end = end.next.next

    # reverse second half
    second, curr = None, mid.next
    mid.next = None # set first half endpoint
    while curr:
        curr.next, second, curr = second, curr, curr.next

    # head -> first half start
    #  second -> second half start (reversed)
    first = head
    while second:
        first.next, second.next, second, first = second, first.next, second.next, first.next