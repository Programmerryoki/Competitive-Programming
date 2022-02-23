import re
print(max(map(len,re.split("[^ATCG]",input()))))

# import re
# print(len(max("".join(re.sub(r"[^ATCG]", " ", input())).split(" "), key=lambda x: len(x))))

# import re
# S = re.sub(r"[^ATCG]", " ", input())
# S = "".join(S).split(" ")
# print(len(max(S, key=lambda x: len(x))))