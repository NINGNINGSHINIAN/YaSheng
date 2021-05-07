# 递增有序表的顺序查找
def sequentialSearch(alist, item):
    position = 0
    found = False
    stop = False
    while position < len(alist) and not found and not stop:
        if alist[position] == item:
            found = True
        elif alist[position] > item:
            stop = True
        else:
            position += 1

    if found:
        return found, position
    else:
        return found


alist = [x + 3 for x in range(1, 11)]
results = []
results = sequentialSearch(alist, 7.5)
print(results)