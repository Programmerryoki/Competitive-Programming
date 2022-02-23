xa,ya,xb,yb,xc,yc = map(int, input().split())
xb,xc = xb-xa,xc-xa
yb,yc = yb-ya,yc-ya
print((abs(xb*yc - yb*xc)/2))