words = []
while True:
    try:
        line = input()
        words += line.split()
    except:
        break

s = set()
for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            s.add(words[i] + words[j])
print("\n".join(sorted(s)))