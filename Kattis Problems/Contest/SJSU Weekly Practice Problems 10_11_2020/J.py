while True:
    s0,s1,r0,r1 = [int(i) for i in input().split()]
    if s0 == s1 == r0 == r1 == 0:
        break

    s = sorted([s0,s1], reverse=True); r = sorted([r0,r1], reverse=True)
    sn = int("".join(map(str, s))); rn = int("".join(map(str, r)))
    if set(s) == set(r):
        print("Tie.")
    elif sn == 21:
        print("Player 1 wins.")
    elif rn == 21:
        print("Player 2 wins.")
    elif len(set(s)) < len(set(r)):
        print("Player 1 wins.")
    elif len(set(s)) > len(set(r)):
        print("Player 2 wins.")
    else:
        print("Player " + ("1 wins." if sn > rn else "2 wins."))