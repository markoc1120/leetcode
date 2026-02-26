from collections import defaultdict

# Time complexity O(n)
# Space complexity O(1) -> a-zA-Z
def minWindow(s: str, t: str) -> str:
    tCount, window = defaultdict(int), defaultdict(int)
    for ch in t:
        tCount[ch] += 1

    have, need = 0, len(tCount)
    best_len = float('inf')
    ans = [-1, -1]
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] += 1

        if c in tCount and window[c] == tCount[c]:
            have += 1
        
        while have == need:
            curr = r - l + 1
            if curr < best_len:
                best_len, ans = curr, [l, r+1]
            
            c = s[l]
            window[c] -= 1
            if c in tCount and window[c] < tCount[c]:
                have -= 1
            l += 1
    l, r = ans
    return s[l:r] if best_len != float('inf') else ''