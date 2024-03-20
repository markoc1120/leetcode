# Time complexity O(n)
# Space complexity O(n)
def reverseWords(s):
    splitted_words = s.split(" ")
    for idx, word in enumerate(splitted_words):
        r, l = 0, len(word) - 1
        rev_word = [0] * len(word)
        while r <= l:
            rev_word[r], rev_word[l] = word[l], word[r]
            r += 1
            l -= 1
        splitted_words[idx] = "".join(rev_word)
    return " ".join(splitted_words)


# Time complexity O(n)
# Space complexity O(n)
def _reverseWords(s):
    return " ".join(word[::-1] for word in s.split(" "))
