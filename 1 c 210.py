v = []
p = []
o = []
while len(v) != 10:
    a = int(input())
    v.append(a)
for i in v:
    if i > 0:
        p.append(i)
    else:
        o.append(i)
print(sum(p))
print(sum(o))