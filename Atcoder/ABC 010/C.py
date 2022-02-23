txa,tya,txb,tyb,T,V = map(int, input().split())
n = int(input())
md = T * V
for _ in range(n):
    x,y = map(int, input().split())
    dis = ((txa-x)**2+(tya-y)**2)**0.5+((txb-x)**2+(tyb-y)**2)**0.5
    if dis <= md:
        print("YES")
        exit()
print("NO")