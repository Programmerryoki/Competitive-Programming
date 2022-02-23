A = input()
B = input()
if int(B)&1:
    ans = (str(int(B)*10//2)+"0"+A)
else:
    ans = (str(int(B)//2)+"0"+A)
print(ans)