from collections import Counter

# Time complexity O(n)
# Space complexity O(m)
def characterReplacement(self, s: str, k: int) -> int:
    counts = Counter()

    max_freq = ans = left = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        max_freq = max(max_freq, counts[s[right]])

        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans