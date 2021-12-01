cp1 = list(map(int,input().split()))
cp2 = list(map(int,input().split()))

xvar = max(cp1[0],cp2[0]) - min(cp1[0],cp2[0])
yvar = max(cp1[1],cp2[1]) - min(cp1[1],cp2[1])

d = ((xvar*xvar)+(yvar*yvar))**0.5

rnd = round(d,2)

print(rnd)
