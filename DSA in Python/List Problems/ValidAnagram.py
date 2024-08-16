def isAnagram(s, t):
    if len(s) != len(t):
        return False
    char_freq = [0] * 26
    for char in s.lower():
        char_freq[ord(char) - 97] += 1
    for char in t.lower():
        char_freq[ord(char) - 97] -= 1
    for freq in char_freq:
        if freq != 0:
            return False
    return True


if __name__ == "__main__":
    s = input("Enter a string: ")
    t = input("Enter a string: ")
    print(isAnagram(s, t))
