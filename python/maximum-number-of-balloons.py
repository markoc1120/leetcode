from collections import Counter

WORD = "balloon"


# Time complexity O(n+m)
# Space complexity O(1) only 26 letters in counts
def maxNumberOfBalloons(text):
    counts = Counter(text)
    word_count = Counter(WORD)

    ans = set()
    for l, count in word_count.items():
        ans.add(counts.get(l, 0) // count)
    return min(ans)
