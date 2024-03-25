from collections import Counter


# Time complexity O(n)
# Space complexity O(n)
def findLucky(arr):
    lucky_nums = set()
    for num, count in Counter(arr).items():
        if num == count:
            lucky_nums.add(num)
    return -1 if not lucky_nums else max(lucky_nums)
