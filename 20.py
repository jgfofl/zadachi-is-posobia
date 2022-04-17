v = []
while True:
    a = float(input())
    if a == 0:
        break
    v.append(a)
maximum = max(v)
k = 0
for i in v:
    if maximum == 1:
        k += 1
print(maximum)
print(k)
