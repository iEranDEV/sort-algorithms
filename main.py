from mergeSort import mergeSort
import utils
import quickSort
import timeit
from heapSort import heapSort
from shellSort import shellSort


algOptions = [
    "Shell sort",
    "Merge sort",
    "Heap sort",
    "Quick sort (rekurencyjny)",
    "Quick sort (iteracyjny)"
]
inputOptions = [
    "Generator danych",
    "Wczytanie z klawiatury"
]


# START PROGRAMU
# Pobranie informacji o oczekiwanej operacji
utils.menu("Wybierz algorytm z listy poniżej.", algOptions)
algType = int(input("Podaj numer algorytmu: "))
print(f'Wybrany algorytm: {algOptions[algType - 1]}')
utils.menu("Wybierz metodę wczytania danych wejściowych.", inputOptions)
inputType = int(input("Podaj numer metody: "))
print(f'Wybrany algorytm: {inputOptions[inputType - 1]}')
data = []

# Pobranie danych wejściowych od użytkownika
if inputType == 1:
    size = int(input("Podaj długość ciągu: "))
    maxValue = int(input("Podaj maksymalną wartość w ciągu: "))
    data = utils.generate(size)
    print("Wygenerowany ciąg:", " ".join(list(map(str, data))))
elif inputType == 2:
    data = list(map(int, input("Podaj ciąg (1 2 3 ...): ").split()))

# Uruchomienie algorytmu zależnie od podanej przez użytkownika wartości
print("-----------")
print(f'Ciąg wejściowy: {data}')
t0 = timeit.default_timer()
if algType == 1:
    shellSort(data)
elif algType == 2:
    data = mergeSort(data)
elif algType == 3:
    heapSort(data, len(data))
elif algType == 4:
    quickSort.quickSortRec(data, 0, len(data) - 1)
elif algType == 5:
    quickSort.quickSortIter(data)
t1 = timeit.default_timer()
print(f'Ciąg wyjściowy: {data}')
print('Czas sortowania: {:.6f}s'.format(t1-t0))
print("-----------")
