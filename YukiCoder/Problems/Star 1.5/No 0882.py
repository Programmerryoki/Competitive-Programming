A,B = [int(i) for i in input().split()]
i = 1
while i * B <= A:
    if A%(i*B) == 0:
        print("YES")
        break
    i += 1
else:
    print("NO")