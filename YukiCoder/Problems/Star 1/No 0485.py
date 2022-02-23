A,B = [int(i) for i in input().split()]
print(B//A if (B/A).is_integer() else "NO")