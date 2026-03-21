class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time complexity O(n)
# Space complexity O(1)
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if max(p.val, q.val) < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
    elif min(p.val, q.val) > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    else:
        return root