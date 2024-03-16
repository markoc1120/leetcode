from collections import Counter


# Time complexity O(m)
# Space complexity O(1) only 26 letters in counts
def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False
    rn = Counter(ransomNote)
    m = Counter(magazine)

    for l, count in rn.items():
        if m.get(l, 0) < count:
            return False
    return True
