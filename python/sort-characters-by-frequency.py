from collections import Counter


# Time complexity O(nlogn)
# Space complexity O(n)
def frequencySort(s):
    counter = Counter(s).most_common()
    ans = []
    for l, count in counter:
        ans.append(l * count)
    return "".join(ans)
