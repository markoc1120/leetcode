# Time complexity O(m*n)
# Space complexity O(m*n)
def maximalSquare(self, matrix: list[list[str]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    cache = {}

    def dfs(r, c):
        if r < 0 or c < 0:
            return 0

        key = (r, c)
        if key not in cache:
            up = dfs(r-1, c)
            diag = dfs(r-1, c-1)
            left = dfs(r, c-1)

            cache[key] = 0
            if matrix[r][c] == '1':
                cache[key] = 1 + min(up, diag, left)
        return cache[key]

    dfs(rows-1, cols-1)
    return max(cache.values())**2