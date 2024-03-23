# Time complexity O(n)
# Space complexity O(1)
def largestAltitude(gain):
    curr = ans = 0
    for alt in gain:
        curr += alt
        ans = max(ans, curr)
    return ans
