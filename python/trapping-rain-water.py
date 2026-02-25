# Time complexity O(n)
# Space complexity O(1)
def trap(height: list[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        leftMax, rightMax = height[left], height[right]

        ans = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                ans += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                ans += rightMax - height[right]
        return ans