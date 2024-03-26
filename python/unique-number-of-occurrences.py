from collections import defaultdict


# Time complexity O(n)
# Space complexity O(n)
def uniqueOccurrences(arr):
    counter = defaultdict(int)
    for num in arr:
        counter[num] += 1

    seen = set()
    for count in counter.values():
        if count in seen:
            return False
        seen.add(count)
    return True
