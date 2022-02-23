X = int(input())

if X - X%100 <= X <= X - X%100 + X//100*5:
    print(1)
else:
    print(0)