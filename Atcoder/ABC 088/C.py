C = [[int(i) for i in input().split()] for j in range(3)]
a = [sum(C[i]) - sum(C[i-1]) for i in range(3)]
b = [sum([C[j][i] for j in range(3)]) - sum([C[j][i-1] for j in range(3)]) for i in range(3)]
for i in range(3):
    if not (a[i]/3).is_integer() or not (b[i]/3).is_integer():
        print("No")
        break
else:
    print("Yes")