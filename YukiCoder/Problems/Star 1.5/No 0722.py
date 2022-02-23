A,B = input().split()
az = A[1:].count("0")
bz = B[1:].count("0")
c1 = (len(set(list(A))) == 2 and A[0] != 0 and az == len(A)-1)
c2 = (len(set(list(A))) == 3 and A[0] == "-" and az == len(A)-2)
c3 = (len(set(list(B))) == 2 and B[0] != 0 and bz == len(B)-1)
c4 = (len(set(list(B))) == 3 and B[0] == "-" and bz == len(B)-2)
if (c1 or c2) and (c3 or c4) and (len(str(abs(int(A)))) > 2 and len(str(abs(int(B)))) > 2):
    print(str(int(A)*int(B))[:-1])
else:
    ab = int(A)*int(B)
    if -99999999 <= ab <= 99999999:
        print(ab)
    else:
        print("E")