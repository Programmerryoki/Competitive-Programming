T = int(input())
for case in range(T):
    N = int(input())
    words = [input().split("*") for i in range(N)]
    for i,w in enumerate(words):
        words[i] = [j for j in w if j !=""]
    words.sort(key=lambda x: len(x))
    print(words)
    ss = words[0]
    s = "".join(ss)
    words = words[1:]
    v = True
    for index in range(N-1):
        line = words[index]
        i = 0
        for w in line:
            # print(w)
            if w == "":
                continue
            if len(w) > len(s):
                for j in ss:
                    if j not in w:
                        break
                else:
                    s = "".join(line)
            j = 0
            while j <= len(w):
                try:
                    temp = s.index(w[:j], i)
                    # print(w[:j], temp)
                except:
                    # print("Beaked")
                    # if j >= len(s[i:])-1:
                    #     s = "".join(line)
                    #     break
                    v = False
                    break
                j += 1
            if not v:
                break
        # print(s)
    if v:
        print("Case #"+str(case+1)+":",s)
    else:
        print("Case #"+str(case+1)+": *")

# T = int(input())
# for case in range(T):
#     N = int(input())
#     s = "*"
#     v = True
#     for _ in range(N):
#         line = input()[::-1]
#         i = 0
#         while i < len(s) and i < len(line):
#             if s[i] == "*":
#                 s = line
#                 break
#             if line[i]=="*":
#                 break
#             if s[i] != line[i]:
#                 v = False
#                 break
#             i += 1
#         # print(i,v)
#     if v:
#         print("Case #"+str(case+1)+":",s[:-1][::-1])
#     else:
#         print("Case #"+str(case+1)+": *")