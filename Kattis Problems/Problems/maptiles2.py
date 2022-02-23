s = input()
print(len(s), int("".join(map(str, [int(i)%2 for i in s])),2), int("".join(map(str, [1 if i not in "01" else 0 for i in s])),2))