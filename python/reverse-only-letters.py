# Time complexity O(n)
# Space complexity O(n)
def reverseOnlyLetters(s):
    r, l, ans = 0, len(s) - 1, list(s)
    while r < l:
        if not ans[r].isalpha():
            r += 1
            continue
        if not ans[l].isalpha():
            l -= 1
            continue
        ans[l], ans[r] = ans[r], ans[l]
        r += 1
        l -= 1

    return "".join(ans)
