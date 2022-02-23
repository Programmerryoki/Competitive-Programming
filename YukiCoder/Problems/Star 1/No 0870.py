N = int(input())
st = [[2,8],[3,9],[7,9]]
end = [[5,8],[4,8],[6,8]]
for a in range(N):
    m = [int(i) for i in input().split()]
    ps = [m[0],m[1]]
    pe = [m[2],m[3]]
    if ps in st:
        st[st.index(ps)] = pe
print("YES") if st == end else print("NO")