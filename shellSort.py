def getHibbard(data):
    i = 1
    przyrost = []
    while True:
        a = pow(2, i) - 1
        i += 1
        if a >= len(data):
            break
        else:
            przyrost.append(a)
    return reversed(przyrost)


def shellSort(data):
    gaps = getHibbard(data)
    for gap in list(gaps):
        for i in range(gap, len(data)):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
