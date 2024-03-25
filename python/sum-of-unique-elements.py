from collections import Counter


# Time complexity O(n)
# Space complexity O(n)
def sumOfUnique(nums):
    uniques = Counter(nums)
    return sum(num for num, count in uniques.items() if count == 1)
