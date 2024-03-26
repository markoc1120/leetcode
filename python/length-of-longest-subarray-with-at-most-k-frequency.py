from collections import defaultdict


# Time complexity O(n)
# Space complexity O(n)
def maxSubarrayLength(nums, k):
    curr = defaultdict(int)
    left = ans = 0
    for right, num in enumerate(nums):
        curr[num] += 1
        while curr[num] > k:
            curr[nums[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans
