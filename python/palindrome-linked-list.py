# Time complexity O(n)
# Space complexity O(1)
def isPalindrome(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    left = None
    curr = slow
    while curr:
        curr.next, left, curr = left, curr, curr.next

    right = head
    while left:
        if right.val != left.val:
            return False
        right = right.next
        left = left.next
    return True
