# Time complexity O(n)
# Space complexity O(1)
def maxVowels(s, k):
    VOWELS = set("aeiou")
    ans = curr = sum(s[i] in VOWELS for i in range(k))
    left = 0
    for right in range(k, len(s)):
        if s[right] in VOWELS:
            curr += 1
        if s[left] in VOWELS:
            curr -= 1

        left += 1
        ans = max(ans, curr)
    return ans
