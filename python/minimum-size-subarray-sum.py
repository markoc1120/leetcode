# Time complexity O(n)
# Space complexity O(1)
def minSubArrayLen(target, nums):
    left = curr = 0
    ans = float("inf")
    for right in range(len(nums)):
        curr += nums[right]
        while curr >= target:
            ans = min(ans, right - left + 1)
            curr -= nums[left]
            left += 1
    return 0 if ans == float("inf") else ans
