# Implementacja algorytmu QUICK SORT REKURENCYJNEGO
def quickSortRec(data, start, end):
    if start < end:
        mid = quickSortPartition(data, start, end)
        quickSortRec(data, start, mid - 1)
        quickSortRec(data, mid + 1, end)


def quickSortPartition(data, start, end):
    pivot = data[end]
    i = start - 1
    for j in range(start, end):
        if data[j] >= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[end] = data[end], data[i + 1]
    return i + 1


def quickSortIter(data):
    stack = [(0, len(data) - 1)]
    while stack:
        start, end = stack.pop()
        if start < end:
            mid = quickSortPartition(data, start, end)
            stack.append((start, mid - 1))
            stack.append((mid + 1, end))

