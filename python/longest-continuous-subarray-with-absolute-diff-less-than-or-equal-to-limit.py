from collections import deque

# Time complexity O(n)
# Space complexity O(n)
def longestSubarray(nums: list[int], limit: int) -> int:
    increasing, decreasing = deque(), deque()

    ans = l = 0
    for r, num in enumerate(nums):
        while increasing and increasing[-1] > num:
            increasing.pop()
        while decreasing and decreasing[-1] < num:
            decreasing.pop()

        increasing.append(num)
        decreasing.append(num)

        while decreasing[0] - increasing[0] > limit:
            l_num = nums[l]
            if l_num == decreasing[0]:
                decreasing.popleft()
            if l_num == increasing[0]:
                increasing.popleft()
            l += 1
        
        ans = max(ans, r-l+1)
    return ans