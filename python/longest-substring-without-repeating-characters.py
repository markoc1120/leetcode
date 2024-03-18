# Time complexity O(n)
# Space complexity O(m) number of unique characters in input
def lengthOfLongestSubstring(s):
    seen = set()
    left = ans = 0

    for right in range(len(s)):
        letter = s[right]
        while letter in seen:
            seen.remove(s[left])
            left += 1
        seen.add(letter)
        ans = max(ans, right - left + 1)
    return ans
