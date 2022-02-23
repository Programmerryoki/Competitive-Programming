from collections import Counter

n,d = map(int, input().split())
a = [int(i) for i in input().split()]
div = [i//d for i in a]
cdiv = Counter(div)
total = 0
for key in cdiv:
    v = cdiv[key]
    total += (v*(v-1) // 2)
print(total)