A = input()
B = input()
if len(A) > len(B):
    print("GREATER")
elif len(A) < len(B):
    print("LESS")
else:
    for i in range(len(A)):
        if int(A) > int(B):
            print("GREATER")
            break
        elif int(A) < int(B):
            print("LESS")
            break
    else:
        print("EQUAL")