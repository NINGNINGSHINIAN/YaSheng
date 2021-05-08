def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    leftHalf = alist[:mid]
    rightHalf = alist[mid:]
    mergeSort(leftHalf)
    mergeSort(rightHalf)
    merged = []
    while leftHalf and rightHalf:
        if leftHalf[0] <= rightHalf[0]:
            merged.append(leftHalf.pop(0))
        else:
            merged.append(rightHalf.pop(0))
    merged.extend(rightHalf if rightHalf else leftHalf)
    return merged


alist = [3, 5, -1, 2, 6]
print(alist)
print(mergeSort(alist))

