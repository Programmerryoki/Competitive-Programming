h1,m1 = [int(i) for i in input().split(":")]
hs1,ms1 = [int(i) for i in input().split(":")]
h2,m2 = [int(i) for i in input().split(":")]
hs2,ms2 = [int(i) for i in input().split(":")]

s1 = h1*60+m1
sh1 = hs1*60+ms1
s2 = h2*60+m2
sh2 = hs2*60+ms2
if s1 < s2:
