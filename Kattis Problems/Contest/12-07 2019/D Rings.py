n = int(input())
while n != -1:
    if n == 0:
        print("The largest component contains 0 rings.")
    else:
        group = [[[float(i) for i in input().split()]]]
        for a in range(n-1):
            connect = []
            ring = [float(i) for i in input().split()]
            for b in range(len(group)):
                for c in group[b]:
                    # finding distance between the center of each rings
                    d = ((c[0] - ring[0])**2 + (c[1] - ring[1])**2)**0.5
                    # if the distance is smaller than the sum of the 2 rings and
                    # one ring is not inside the other ring, then those rings are connected
                    if d < ring[2]+c[2] and d + c[2] > ring[2] and d + ring[2] > c[2]:
                        connect.append(b)
                        break
            if len(connect) == 0:
                group.append([ring])
            else:
                # connecting groups of rings that the new ring has created
                temp = [ring]
                for i in connect[::-1]:
                    temp += group.pop(i)
                group.append(temp)
        ma = max([len(i) for i in group])
        if ma == 1:
            print("The largest component contains 1 ring.")
        else:
            print("The largest component contains",ma,"rings.")
    n = int(input())