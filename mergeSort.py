# Implementacja algorytmu MERGE SORT
def mergeSort(data):
    if len(data) <= 1:
        return data
    middleIndex = len(data) // 2
    leftSide = data[:middleIndex]
    rightSide = data[middleIndex:]
    return merge(mergeSort(leftSide), mergeSort(rightSide))


def merge(leftSide, rightSide):
    result = []
    while len(leftSide) > 0 and len(rightSide) > 0:
        if leftSide[0] > rightSide[0]:
            result.append(leftSide[0])
            leftSide.pop(0)
        else:
            result.append(rightSide[0])
            rightSide.pop(0)
    if leftSide:
        result += leftSide
    if rightSide:
        result += rightSide
    return result

