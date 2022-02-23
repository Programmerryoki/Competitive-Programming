ct = input()
key = input()
word = ""
for i in range(len(ct)):
    w = chr((ord(ct[i]) - ord(key[i]) + 26) % 26 + ord("A"))
    key += w
    word += w
print(word)