t = int(input())
for _ in range(t):
    S = input()
    z = S.count("0")
    print("DA") if min(z, len(S) - z)%2 == 1 else print("NET")

    # pos = {S}
    # d = 0
    # win = False
    # seen = {S}
    # while pos:
    #     new = set()
    #     while pos:
    #         s = pos.pop()
    #         has = False
    #         for i in range(len(s)-1):
    #             # print(s[i:i+2])
    #             if s[i:i+2] in "101":
    #                 has = True
    #                 string = s[:i]+s[i+2:]
    #                 if string not in seen:
    #                     new.add(string)
    #                     seen.add(string)
    #         if not has and d%2 == 1:
    #             win = True
    #             break
    #         d += 1
    #     # print(new)
    #     pos = new
    #     if win:
    #         break
    # print("DA") if win else print("NET")