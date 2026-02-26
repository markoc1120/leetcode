# Time complexity O(n)
# Space complexity O(1)
def checkInclusion(s1: str, s2: str) -> bool:
    s1_n, s2_n = len(s1), len(s2)
    if s1_n > s2_n:
        return False

    s1Count, s2Count = [0]*26, [0]*26
    start = ord('a')
    for i in range(s1_n):
        s1Count[ord(s1[i]) - start] += 1
        s2Count[ord(s2[i]) - start] += 1
    
    matches = 0
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    l = 0
    for r in range(s1_n, s2_n):
        if matches == 26:
            return True
        
        index = ord(s2[r]) - start
        s2Count[index] += 1
        if s2Count[index] == s1Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - start
        s2Count[index] -= 1
        if s2Count[index] == s1Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
    return matches == 26