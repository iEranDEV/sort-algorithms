from mergeSort import mergeSort
import utils
import quickSort
import timeit
import sys
import math
from heapSort import heapSort
from shellSort import shellSort

sys.setrecursionlimit(10**6)

sizes = [20, 250, 500, 1000, 2000, 5000, 10000, 20000, 35000, 50000]
arrTypes = ['losowy', 'rosnący', 'malejący', 'v-kształtny', 'a-kształtny']
algTypes = ['mergeSort', 'shellSort', 'quickItSort', 'heapSort']

arrays = {}
ile_ciagow = 5

# Generowanie ciągów
for arrType in arrTypes:
    arrays[arrType] = {}
    for size in sizes:
        arrays[arrType][size] = []
        for i in range(ile_ciagow):
            temp = []
            if arrType == 'losowy':
                temp = utils.generate(size)
            elif arrType == 'rosnący':
                temp = utils.generate_increasing_sequence(size)
            elif arrType == 'malejący':
                temp = utils.generate_decreasing_sequence(size)
            elif arrType == 'v-kształtny':
                temp = utils.generate_v_shaped_sequence(size)
            elif arrType == 'a-kształtny':
                temp = utils.generate_a_shaped_sequence(size)
            arrays[arrType][size].append(temp)

# Uruchamianie algorytmów i testowanie czasu
for algType in algTypes:
    print(f'ALGORYTM : {algType}')
    for size in sizes:
        print(f'  SIZE : {size}')
        for arrType in arrTypes:
            times = []
            for temp in arrays[arrType][size]:
                data = temp[:]
                t0 = timeit.default_timer()
                if algType == 'shellSort':
                    shellSort(data)
                elif algType == 'mergeSort':
                    data = mergeSort(data)
                elif algType == 'heapSort':
                    heapSort(data, len(data))
                elif algType == 'quickRecSort':
                    quickSort.quickSortRec(data, 0, len(data) - 1)
                elif algType == 'quickItSort':
                    quickSort.quickSortIter(data)
                t1 = timeit.default_timer()
                times.append(t1-t0)
            sum = 0
            for time in times:
                sum += time
            avg = sum / ile_ciagow
            odchylenie = 0
            for time in times:
                odchylenie += (time - avg)**2
            odchylenie = math.sqrt(odchylenie / len(times))
            print('    typ {type} : {time:.6f}s, ({odchylenie:.6f})'.format(type=arrType, time=(avg), odchylenie=odchylenie))
