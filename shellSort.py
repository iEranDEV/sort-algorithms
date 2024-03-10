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
        for i in range(0, gap):
            values = []
            for j in range(i, len(data), gap):
                values.append(data[j])
            if len(values) != 1:
                for k in range(1, len(values)):
                    key = values[k]
                    m = k - 1
                    while m >= 0 and key < values[m]:
                        values[m + 1] = values[m]
                        m -= 1
                    values[m + 1] = key
                for j in range(i, len(data), gap):
                    data[j] = values[0]
                    values = values[1:]
            i += 1
        print(f'Ciąg dla przyrostu {gap}: {data}')

