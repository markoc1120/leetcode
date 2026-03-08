# Time complexity O(n)
# Space complexity O(n)
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []

    ans = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            ans[j] = i - j
        
        stack.append(i)
    return ans