t,p = [int(i) for i in input().split()]
# Assume only 1 parent
graph = {}
for _ in range(t):
    name, *rest = input().split()
    child = rest[1:]
    for c in child:
        graph[c] = name

for _ in range(p):
    s1,s2 = input().split()
    n1,n2 = [], []
    t1 = s1
    t2 = s2
    while True:
        if t1 == t2:
            break
        if t2 in n1:
            n1 = n1[:n1.index(t2)]
            break
        if t1 in n2:
            n2 = n2[:n2.index(t1)]
            break
        if t1 != "" and t1 not in n1:
            n1.append(t1)
            if t1 in graph:
                t1 = graph[t1]
            else:
                t1 = ""
        if t2 not in n2 and t2 != "":
            n2.append(t2)
            if t2 in graph:
                t2 = graph[t2]
            else:
                t2 = ""
    if t1 == "" and t2 == "":
        for i in n1:
            if i in n2:
                n2 = n2[:n2.index(i)]
        for i in n2:
            if i in n1:
                n1 = n1[:n1.index(i)]

    if len(n1) == 0 or len(n2) == 0:
        if len(n1) == 0:
            if len(n2) == 1:
                print(f"{s2} is the child of {s1}")
            else:
                print(f"{s2} is the {'great '*(len(n2)-2)}grandchild of {s1}")
        else:
            if len(n1) == 1:
                print(f"{s1} is the child of {s2}")
            else:
                print(f"{s1} is the {'great '*(len(n1)-2)}grandchild of {s2}")
    elif len(n1) == len(n2):
        if len(n1) == 1:
            print(f"{s1} and {s2} are siblings")
        else:
            rank = str(len(n1)-1)
            if rank[-1] == "1":
                rank += "st"
            elif rank[-1] == "2":
                rank += "nd"
            elif rank[-1] == "3":
                rank += "rd"
            else:
                rank += "th"
            print(f"{s1} and {s2} are {rank} cousins")
    else:
        rank = str(min(len(n1), len(n2)) - 1)
        if rank[-1] == "1":
            rank += "st"
        elif rank[-1] == "2":
            rank += "nd"
        elif rank[-1] == "3":
            rank += "rd"
        else:
            rank += "th"
        remove = str(max(len(n1), len(n2)) - min(len(n1), len(n2)))
        print(f"{s1} and {s2} are {rank} cousins, {remove} {'time' if remove == '1' else 'times'} removed")