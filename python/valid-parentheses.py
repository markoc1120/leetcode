# Time complexity O(n)
# Space complexity O(n)
def isValid(s: str) -> bool:
    mapping = {'(': ')', '{': '}', '[': ']'}

    stack = []
    for ch in s:
        if ch in mapping:
            stack.append(ch)
        else:
            if not stack:
                return False
            
            prev_opening = stack.pop()
            if mapping[prev_opening] != ch:
                return False
    return not stack