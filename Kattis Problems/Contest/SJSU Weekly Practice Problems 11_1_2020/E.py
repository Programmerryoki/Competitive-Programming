N,L = map(int, input().split())
if N == L and L == 1:
    print("LADICA")
    exit()
store = [-1]*L
items = []
ans = []
for i in range(N):
    # print(store)
    A,B = [int(i)-1 for i in input().split()]
    # print(i,A,B)
    items.append((A,B))
    if store[A] == -1:
        store[A] = i
        ans.append("LADICA")
        continue
    if store[B] == -1:
        store[B] = i
        ans.append("LADICA")
        continue
    # print(items)
    temp = A
    order = []
    seen = {A}
    while store[temp] != -1:
        p = store[temp]
        temp = items[p][1-items[p].index(temp)]
        if temp in seen:
            break
        order.append(temp)
        seen.add(temp)
    else:
        # print(temp, seen, order)
        p = store[A]
        store[A] = i
        for j in order:
            p,store[j] = store[j],p
        ans.append("LADICA")
        continue
    # print(temp, seen, order)
    temp = B
    order = []
    seen = {B}
    while store[temp] != -1:
        p = store[temp]
        temp = items[p][1-items[p].index(temp)]
        if temp in seen:
            break
        order.append(temp)
        seen.add(temp)
    else:
        # print(temp, seen, order)
        p = store[B]
        store[B] = i
        for j in order:
            p,store[j] = store[j],p
        ans.append("LADICA")
        continue
    ans.append("SMECE")
# print(store)
print(*ans, sep="\n")