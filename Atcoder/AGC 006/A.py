N = int(input())
s = input()
t = input()
for i in range(N):
    if s[i:] == t[:N-i]:
        print(N+i)
        exit()
print(N*2)

# N = int(input())
# s = input()
# t = input()
# s = s[::-1]
# ml = len(s) + len(t)
# same = ""
# for i in range(min(len(s),len(t))):
#     if s[:i] != same or t[:i] != same:
#         print(s[:i], t[:i], same)
#         ml = min(ml, len(s) + len(t) - len(same))
#         break
#     else:
#         same += s[i]
# print(ml)