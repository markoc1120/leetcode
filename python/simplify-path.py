# Time complexity O(n)
# Space complexity O(n)
def simplifyPath(path: str) -> str:
    stack = []

    for p in path.split('/'):
        if not p or p == '.':
            continue
        elif p == '..':
            if stack:
                stack.pop()
        else:
            stack.append(p)
    return f"/{'/'.join(stack)}"