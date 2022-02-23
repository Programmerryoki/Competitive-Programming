n = int(input())
a = [int(i)%360 for i in input().split()]
b = [int(i)%360 for i in input().split()]
a.sort()
a = [a[0]+360-a[-1]] + [a[i+1] - a[i] for i in range(n-1)]
b.sort()
b = [b[0]+360-b[-1]] + [b[i+1] - b[i] for i in range(n-1)]
sa = " ".join(map(str, a))
sa = sa + " " + sa
sb = " ".join(map(str, b))
# print(sa,sb)
print("possible" if sb in sa else "impossible")