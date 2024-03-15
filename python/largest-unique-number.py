from collections import Counter, defaultdict


# Time complexity O(n)
# Space complexity O(n)
def largestUniqueNumber(nums):
    counts, ans = Counter(nums), -1
    for num, count in counts.items():
        if count == 1:
            ans = max(ans, num)
    return ans


def _largestUniqueNumber(nums):
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1

    ans = -1
    for num, count in counts.items():
        if count == 1:
            ans = max(ans, num)
    return ans
