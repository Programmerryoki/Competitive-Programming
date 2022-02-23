n = [int(input()) for i in range(5)]
m = min(n, key=lambda x: (x + 9) % 10)
n.remove(m)
print(sum([(i+9)//10 * 10 for i in n]) + m)