class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time complexity O(n)
# Space complexity O(1)
def hasCycle(head: ListNode | None) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    