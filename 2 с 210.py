ar = [1, 2, 3, 4, 5 ]
def check_sort(array):
    rise = "True"
    wane = "True"
    for i in range (len(ar) - 1):
        if ar[i] <= ar[i + 1]:
            wane = "False"
            
        elif ar[i] >= ar[i + 1]:
            rise = "False"
        return rise or wane

print(check_sort(ar))


