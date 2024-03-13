# Time complexity O(n)
# Space complexity O(n)
def getAverages(nums, k):
    n = len(nums)
    ans = [-1] * n
    window_size = 2 * k + 1
    if k > n:
        return ans

    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[i - 1] + nums[i])

    for i in range(k, n - k):
        ans[i] = (prefix_sum[i + k] - prefix_sum[i - k] + nums[i - k]) // window_size
    return ans
