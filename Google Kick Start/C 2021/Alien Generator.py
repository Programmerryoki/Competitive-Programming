T = int(input())
for case in range(T):
    G = int(input())
    ans = 0
    cum = 0
    for i in range(1,10**7):
        calc = (G - cum) / i
        if calc != 0 and calc.is_integer():
            # print(i,cum)
            ans += 1
        cum += i
        if cum > G:
            break
    print(f"Case #{case+1}: {ans}")