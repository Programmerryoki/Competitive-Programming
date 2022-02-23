V,T,S,D = [int(i) for i in input().split()]
print("Yes" if not (V*T <= D <= V*S) else "No")