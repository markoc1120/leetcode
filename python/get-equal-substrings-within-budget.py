# Time complexity O(n)
# Space complexity O(1)
def equalSubstring(s, t, maxCost):
    def get_diff(l1, l2):
        return abs(ord(l1) - ord(l2))

    left = curr = ans = 0
    for right in range(len(s)):
        curr += get_diff(s[right], t[right])
        while curr > maxCost:
            curr -= get_diff(s[left], t[left])
            left += 1
        ans = max(ans, right - left + 1)
    return ans
