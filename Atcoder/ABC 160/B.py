X = int(input())
h = X//500 * 1000
X = X%500
h += X//5 * 5
print(h)