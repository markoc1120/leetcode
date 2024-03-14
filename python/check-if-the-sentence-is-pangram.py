# Time complexity O(n)
# Space complexity O(1)
def checkIfPangram(sentence):
    return len(set(sentence)) == 26
