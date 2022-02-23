vowel = "aeiouAEIOU"

line = input().split()
for i in range(len(line)):
    a = line[i]
    b = 1
    while b < len(a) - 1:
        if a[b] == "p" and a[b-1] in vowel and  a[b-1] == a[b+1]:
            a = a[:b] + a[b+2:]
        b += 1
    line[i] = a
print(" ".join(line))