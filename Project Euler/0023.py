abu = []
for n in range(1, 28123):
    s = 0
    for i in range(1, n):
        if n%i == 0:
            s += i
    if s > n:
        abu.append(n)
print('abu done')

sa = set(abu)
total = 0
for n in range(1, 28123):
    for a in abu:
        if n - a in sa:
            break
    else:
        print(n)
        total += n
print(total)