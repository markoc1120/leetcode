from collections import Counter


# Time complexity O(n)
# Space complexity O(1) only 26 letters in both jewels and stones
def numJewelsInStones(jewels, stones):
    jewels_set = set(jewels)
    stones_counter = Counter(stones)

    ans = 0
    for j in jewels_set:
        ans += stones_counter.get(j, 0)
    return ans


def _numJewelsInStones(jewels, stones):
    jewels_set = set(jewels)
    return sum(s in jewels_set for s in stones)
