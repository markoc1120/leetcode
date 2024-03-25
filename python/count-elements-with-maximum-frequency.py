from collections import Counter


# Time complexity O(n)
# Space complexity O(n)
def maxFrequencyElements(nums):
    counter = Counter(nums).most_common()
    _max = counter[0][1]
    return sum(count for _, count in counter if count == _max)
