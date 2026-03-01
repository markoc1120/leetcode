# Time complexity O(n)
# Space complexity O(n)
def makeGood(s: str) -> str:
    diff = ord('a') - ord('A')
    stack = []
    for ch in s:
        if stack and abs(ord(stack[-1]) - ord(ch)) == diff:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)