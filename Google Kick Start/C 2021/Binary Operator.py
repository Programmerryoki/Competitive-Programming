from collections import Counter
import re

operator = {"+","*","#"}

def breaker(rem):
    elem = []
    ope = []
    i = 0
    while i < len(rem):
        if rem[i] == "(":
            t = 1
            while t != 0:
                i += 1
                if rem[i] == "(":
                    t += 1
                elif rem[i] == ")":
                    t -= 1
            i += 1
            continue
        if rem[i] in operator:
            elem.append(rem[:i])
            ope.append(rem[i])
            rem = rem[i+1:]
            i = -1
        i += 1
    elem.append(rem)
    return [elem,ope]

def is_int(string):
    try:
        int(string)
        return True
    except:
        return False

def add_dict(dict1, dict2):
    rdic = {}
    for key in dict1:
        if key in dict2:
            rdic[key] = add_dict(dict1[key] + dict2[key])
        else:
            rdic[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            rdic[key] = dict2[key]
    return rdic

def breaking(paran):
    paran = paran[1:-1]
    para = re.findall(r"\(.+\)", paran)
    print("para:",para)
    dic = {}
    for p in para:
        print(p)
        if p in dic:
            dic[p].update(breaking(p))
        else:
            dic[p] = breaking(p)
    # print(paran)
    print("dic",dic)
    elem,ope = breaker(paran)
    if len(elem) == 1:
        return dic
    print("elem and ope",elem, ope)
    e1,e2 = elem
    if ope[0] == "+":
        if is_int(e1) and is_int(e2):
            if 1 in dic:
                dic[1] += int(e1) + int(e2)
            else:
                dic[1] = int(e1) + int(e2)
        elif is_int(e1):
            name = "("+e1+"#"+e2+")"
        elif is_int(e2):
        else:
    elif ope[0] == "*":
        if is_int(e1) and is_int(e2):
        elif is_int(e1):
        elif is_int(e2):
        else:
    elif ope[0] == "#":
        name = "("+e1+"#"+e2+")"
        dic[name] = add_dict(dic[e1], dic[e2])

    return {}

T = int(input())
for case in range(T):
    N = int(input())
    lines = [breaking(input()) for i in range(N)]
    print(lines)
    Clines = [lines.count(i) for i in lines]
    order = list(sorted(Clines))
    print("--------\n",order)