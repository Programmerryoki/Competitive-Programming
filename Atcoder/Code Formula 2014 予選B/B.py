N = input()
odd = 0
even = 0
for i,d in enumerate(N[::-1]):
    if i&1:
        odd += int(d)
    else:
        even += int(d)
print(odd, even)