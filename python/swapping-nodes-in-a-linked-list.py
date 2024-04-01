# Time complexity O(n)
# Space complexity O(1)
def swapNodes(head, k):
    right, fast = head, head
    while k > 1:
        fast = fast.next
        k -= 1

    left = fast
    while fast.next:
        fast = fast.next
        right = right.next
    left.val, right.val = right.val, left.val
    return head
