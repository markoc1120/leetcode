# Time complexity O(n)
# Space complexity O(n)
def reversePrefix(word, ch):
    l = r = 0
    while l < len(word):
        if word[l] == ch:
            break
        l += 1

    if l == len(word):
        return word

    word_list = list(word)
    while r < l:
        word_list[r], word_list[l] = word_list[l], word_list[r]
        r += 1
        l -= 1
    return "".join(word_list)
