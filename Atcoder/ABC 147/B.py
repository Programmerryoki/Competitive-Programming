s = input()
sp = s[::-1]
diff = [1 for i in range(len(s)) if s[i] != sp[i]]
print(sum(diff)//2)
# print(s)
# print(sp)
# print(diff)