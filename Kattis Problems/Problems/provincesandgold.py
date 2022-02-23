G, S, C = [int(i) for i in input().split()]
money = G*3 + S*2 + C*1
vc = [[8, "Province"], [5, "Duchy"], [2, "Estate"]]
tc = [[6, "Gold"], [3, "Silver"], [0, "Copper"]]
v = 0
while v < len(vc) and vc[v][0] > money:
    v += 1
t = 0
while t < len(tc) and tc[t][0] > money:
    t += 1

print(vc[v][1], "or", tc[t][1]) if v < len(vc) else print(tc[t][1])