from collections import defaultdict


# Time complexity O(nlogn)
# Space complexity O(n)
def findWinners(matches):
    losses = defaultdict(int)
    for winner, loser in matches:
        losses[winner] = losses.get(winner, 0)
        losses[loser] += 1

    winner_ans, loser_ans = [], []
    for p in losses:
        if not losses.get(p):
            winner_ans.append(p)
        if losses.get(p) == 1:
            loser_ans.append(p)

    return [sorted(winner_ans), sorted(loser_ans)]
