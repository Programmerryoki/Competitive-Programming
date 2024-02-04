total = 0
pow = 5
for n in range(2, 10**6):
    if n == sum(int(i)**pow for i in str(n)):
        total += n
        print(n)
print(total)