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


# Time complexity O(1)
# Space complexity O(n)
def _numSubarraysWithSum(nums, goal):
    prefix_zeros = 0
    left = curr = ans = 0
    for right, num in enumerate(nums):
        curr += num
        while left < right and (nums[left] == 0 or curr > goal):
            if nums[left] == 1:
                prefix_zeros = 0
            else:
                prefix_zeros += 1

            curr -= nums[left]
            left += 1
        if curr == goal:
            ans += 1 + prefix_zeros
    return ans
