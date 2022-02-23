a,b = [int(i) for i in input().split()]
if a + 1 <= b:
    print("YES")
else:
    print("NO")
print(abs(b-a-1))