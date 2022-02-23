A = input()
B = input()
m = min(len(A),len(B)); ma = max(len(A), len(B))
AL = 0 if len(A) < len(B) else 1 if len(A) == len(B) else 2
A = " "*(ma - len(A)) + A
B = " "*(ma - len(B)) + B
i = 0
dif = 0
while i < len(A):
# for i in range(len(A)):
    print(A,B)
    if A[i] == " " or B[i] == " ":
        continue
    if int(A[i]) + int(B[i]) >= 10:
        num = int("1"+"0"*(ma-i))
        if i == len(A) - m:
            print("top",AL)
            if AL == 0:
                dif = min(int(A), num - int(B[i:]))
            elif AL == 1:
                ia = int(A); ib = int(B)
                dif = min(ia,ib,num-ia,num-ib)
            elif AL == 2:
                dif = min(int(B), num - int(A[i:]))
        else:
            dif = min(int(A[i:]),int(B[i:]),num - int(A[i:]), num - int(B[i:]))
        i -= 2
        # print(dif)
        # break
    i += 1
print(dif)