from collections import defaultdict


# Time complexity O(n)
# Space complexity O(n)
def findMaxLength(nums):
    prefix_sum = defaultdict(int)
    prefix_sum[0] = -1
    curr = ans = 0

    for i in range(len(nums)):
        curr += 1 if nums[i] == 1 else -1
        if curr in prefix_sum:
            ans = max(ans, i - prefix_sum[curr])
        else:
            prefix_sum[curr] = i
    return ans
