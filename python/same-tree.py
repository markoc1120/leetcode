
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity O(n)
# Space complexity O(1)
def isSameTree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p and not q:
        return True

    if (not p or not q) or (p.val != q.val):
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)