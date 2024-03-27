from collections import defaultdict


# Time complexity O(n)
# Space complexity O(n)
def numIdenticalPairs(nums):
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1
    return sum((count * (count - 1)) // 2 for count in counter.values())
