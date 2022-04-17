lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst12 = lst1 + lst2
lst12.sort()
print(*lst12)

