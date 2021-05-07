def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if item == alist[middle]:
            found = True
        elif item > alist[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if found:
        return found, middle
    else:
        return found


alist = [x + 3 for x in range(1, 11)]
print(alist)
results = []
results = binarySearch(alist, 13)
print(results)
