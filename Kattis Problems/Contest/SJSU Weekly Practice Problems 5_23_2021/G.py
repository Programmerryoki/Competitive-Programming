while True:
    A,B = map(int, input().split())
    if A == 0 and B == 0:
        break

    table = [["0"*(2 - len(str(int(i)*int(j))))+str(int(i)*int(j)) for i in str(A)] for j in str(B)]
    ans = str(A*B)
    # print(table)
    # print(ans)
    la = len(str(A))
    lb = len(str(B))
    lans = len(str(ans))
    print("+"+"-"*(3+4*la)+"+")
    print("|   "+"   ".join(str(A))+"   |")
    for i,numb in enumerate(str(B)):
        print("| "+"+---"*la+"+ |")
        print("|"+("/" if lb-i < lans-la else " ")+"|"+" /|".join([str(j)[0] for j in table[i]])+" /| |")
        print("| "+"| / "*la+"|"+numb+"|")
        print("|"+(str(ans)[i-(la+lb-lans)] if lb-i-1 < lans-la else " ")+"|/ "+"|/ ".join([str(j)[1] for j in table[i]])+"| |")
    print("| "+"+---"*la+"+ |")
    print("|"+("/" if lans > la else " ")+" "+" / ".join([i for i in ans[lans-la:]])+"    |")
    print("+"+"-"*(3+4*la)+"+")