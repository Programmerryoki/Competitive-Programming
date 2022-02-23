A, B = input(), input()
try:
    int(A), int(B)
    if len(A) == len(str(int(A))) and len(B) == len(str(int(B))) and 0 <= int(A) <= 12345 and 0 <= int(B) <= 12345:
        print("OK")
    else:
        print("NG")
except:
    print("NG")