from itertools import permutations

K = int(input())
count = 0
for num in permutations([str(i) for i in range(1,9)], 8):
    n = "".join(num)
    if int(n) % K == 0:
        count += 1
print(count)