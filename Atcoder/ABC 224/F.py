MOD = 998244353

S = input()
total = 0
mul2 = [2]
for i in range(19):
    mul2.append(mul2[-1]**2 % MOD)
# print(mul2)
for l in range(1,len(S)+1):
    for i in range(len(S)-l+1):
        # print(S[i:i+l])
        num = int(S[i:i+l]) % MOD
        am = max(0,len(S)-l-i-1)
        n = bin(am)[2:][::-1]
        af = 1
        for j in range(len(n)):
            if n[j] == "1":
                af *= mul2[j]
                af %= MOD
        bm = max(0,i)
        n = bin(bm)[2:][::-1]
        bf = 1
        for j in range(len(n)):
            if n[j] == "1":
                bf *= mul2[j]
                bf %= MOD
        # print(am, bm)
        total += num * af * bf
        total %= MOD
print(total)