from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity O(n)
# Space complexity O(n)
def levelOrder(root: TreeNode | None) -> list[list[int]]:
    queue = deque([root])
    ans = []

    while queue:
        nodes_left = len(queue)
        subans = []

        for _ in range(nodes_left):
            node = queue.popleft()
            if node:
                subans.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if subans:
            ans.append(subans)
    return ans