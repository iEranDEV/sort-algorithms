# Implementacja algorytmu HEAP SORT
def kopcowanie(data, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and data[left] < data[smallest]:
        smallest = left
    if right < n and data[right] < data[smallest]:
        smallest = right
    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        kopcowanie(data, n, smallest)


def heapSort(data, n):
    for i in range(int(n / 2) - 1, -1, -1):
        kopcowanie(data, n, i)
    for i in range(n-1, -1, -1):
        data[0], data[i] = data[i], data[0]
        kopcowanie(data, i, 0)

