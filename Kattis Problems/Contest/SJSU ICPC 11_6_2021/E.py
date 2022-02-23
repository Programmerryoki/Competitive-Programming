MOD = 10**9 + 9

N = input()
tnf = 1
p = False
for i in range(len(N)):
    if N[i] != "0":
        p = True
    else:
        if p:
            tnf *= 2
            tnf %= MOD
print(max(1, tnf+1))

"""
1011 => 2
1010 => 5
"""