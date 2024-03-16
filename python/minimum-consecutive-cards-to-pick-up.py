from collections import defaultdict


# Time complexity O(n)
# Space complexity O(n)
def minimumCardPickup(cards):
    """
    :type cards: List[int]
    :rtype: int
    """
    inc_positions = defaultdict(int)
    ans = float("inf")
    for i, card in enumerate(cards):
        if card in inc_positions:
            ans = min(ans, i - inc_positions[card] + 1)
        inc_positions[card] = i
    return -1 if ans == float("inf") else ans
