from collections import defaultdict


# Time complexity O(n)
# Space complexity O(n)
def numSubarraysWithSum(nums, goal):
    prefix_sum = defaultdict(int)
    curr = ans = 0

    for num in nums:
        curr += num
        if curr == goal:
            ans += 1
        if curr - goal in prefix_sum:
            ans += prefix_sum[curr - goal]
        prefix_sum[curr] += 1
    return ans
