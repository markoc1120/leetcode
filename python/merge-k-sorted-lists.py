class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeList(a, b: ListNode) -> ListNode:
    dummy = ListNode(0)
    res = dummy
    while a and b:
        if a.val < b.val:
            dummy.next = a
            a = a.next
        else:
            dummy.next = b
            b = b.next
        dummy = dummy.next

    if a:
        dummy.next = a
    elif b:
        dummy.next = b
    return res.next

# Time complexity O(n*k)
# Space complexity O(1)
def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
    for i in range(1, len(lists)):
        lists[i] = mergeList(lists[i-1], lists[i])
    return lists[-1] if lists else None