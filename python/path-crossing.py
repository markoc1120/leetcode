# Time complexity O(n)
# Space complexity O(n)
def isPathCrossing(path):
    x = y = 0
    coordinates = set()
    coordinates.add((x, y))
    for path in path:
        if path == "N":
            x += 1
        elif path == "S":
            x -= 1
        elif path == "E":
            y += 1
        else:
            y -= 1

        if (x, y) in coordinates:
            return True
        coordinates.add((x, y))
    return False
