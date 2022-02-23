d = ["Sun","Sat"]
s1, s2 = input().split()
if s1 in d and s2 in d:
    print("8/33")
elif s1 in d:
    print("8/32")
else:
    print("8/31")