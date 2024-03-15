# Time complexity O(n)
# Space complexity O(n)
def countElements(arr):
    counter = {}
    for el in arr:
        if el not in counter:
            counter[el] = 1
        else:
            counter[el] += 1

    ans = 0
    for el in arr:
        if el + 1 in counter:
            ans += 1
    return ans


# Time complexity O(n)
# Space complexity O(n)
def _countElements(arr):
    unique_nums = set(arr)
    ans = 0
    for el in arr:
        if el + 1 in unique_nums:
            ans += 1
    return ans
