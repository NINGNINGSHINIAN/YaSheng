# 无序表的顺序查找
def sequentialSearch(alist, item):
    found = False
    position = 0
    while position < len(alist) and not found:
        if alist[position] == item:
            found = True
        else:
            position += 1

    if found:
        return found, position
    else:
        return found


alist = [x + 3 for x in range(1, 11)]
results = []
results = sequentialSearch(alist, 8)
print(results)
