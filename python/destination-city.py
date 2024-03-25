# Time complexity O(n)
# Space complexity O(n)
def destCity(paths):
    starts = set()
    for start, _ in paths:
        if start not in starts:
            starts.add(start)

    for _, end in paths:
        if end not in starts:
            return end
