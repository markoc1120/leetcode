# Time complexity O(n)
# Space complexity O(1)
def deleteDuplicates(head):
    if not head:
        return head

    curr = head
    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next
    return head
