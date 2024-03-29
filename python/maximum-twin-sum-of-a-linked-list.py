# Time complexity O(n)
# Space complexity O(1)
def pairSum(head):
    fast, middle = head, head
    while fast and fast.next:
        middle = middle.next
        fast = fast.next.next

    prev, curr = None, middle
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    ans = 0
    while prev:
        ans = max(ans, prev.val + head.val)
        prev, head = prev.next, head.next
    return ans
