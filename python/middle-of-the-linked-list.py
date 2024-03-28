# Time complexity O(n)
# Space complexity O(1)
def middleNode(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
