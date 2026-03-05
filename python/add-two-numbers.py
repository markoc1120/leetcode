class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity O(m + n)
# Space complexity O(1)  extra space
def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    rem = 0
    sentinel = ans = ListNode()

    while l1 or l2 or rem:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        _sum = v1 + v2 + rem
        ans.next = ListNode(_sum % 10)
        rem = _sum // 10

        ans = ans.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return sentinel.next