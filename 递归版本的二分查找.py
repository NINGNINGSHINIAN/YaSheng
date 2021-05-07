def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        middle = len(alist) // 2
        if item == alist[middle]:
            return True
        elif item > alist[middle]:
            return binarySearch(alist[middle + 1:], item)
        else:
            return binarySearch(alist[:middle], item)


alist = [x + 3 for x in range(1, 11)]
print(alist)
results = []
results = binarySearch(alist, 7.5)
print(results)