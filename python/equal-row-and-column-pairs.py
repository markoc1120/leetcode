from collections import defaultdict


# Time complexity O(n2)
# Space complexity O(n)
def equalPairs(grid):
    rows = defaultdict(int)
    for row in grid:
        rows[tuple(row)] += 1

    columns = defaultdict(int)
    for row in range(len(grid[0])):
        column = []
        for col in range(len(grid)):
            column.append(grid[col][row])
        columns[tuple(column)] += 1

    return sum(rows[col] * columns[col] for col in columns)
