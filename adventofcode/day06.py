cp = lambda x: ord(x) - ord('a')

char = input()
seen = [0]*26
for c in char[:13]:
    seen[cp(c)] += 1
for i in range(13, len(char)):
    seen[cp(char[i])] += 1
    if seen.count(1) != 14:
        seen[cp(char[i-13])] -= 1
        continue
    print(i+1)
    break

# cp = lambda x: ord(x) - ord('a')
#
# char = input()
# seen = [0]*26
# for c in char[:3]:
#     seen[cp(c)] += 1
# for i in range(3, len(char)):
#     seen[cp(char[i])] += 1
#     if seen.count(1) != 4:
#         seen[cp(char[i-3])] -= 1
#         continue
#     print(i+1)
#     break