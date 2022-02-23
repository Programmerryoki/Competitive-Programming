rules = [("01","2"),("12","3"),("23","4"),("34","5"),("45","6"),
         ("56","7"),("67","8"),("78","9"),("89","0"),("90","1")]

T = int(input())
for case in range(T):
    N = int(input())
    S = list(input())
    while True:
        change = False
        for replace, to in rules:
            r1,r2 = replace[0],replace[1]
            i = 0
            while i < len(S):
                if i < len(S)-1 and S[i]==r1 and S[i+1]==r2:
                    S[i:i+2] = to
                    change = True
                else:
                    i += 1
        if not change:
            break
    print(f"Case #{case+1}: {''.join(S)}")