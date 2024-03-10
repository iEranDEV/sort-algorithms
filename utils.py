import random


# Wysłanie menu z wyborem dla użytkownika
def menu(title, options):
    print("-----------")
    print(title)
    for index, option in enumerate(options):
        print(f'  [{index + 1}.] {option}')
    print("-----------")


# Generowanie losowego ciągu liczb
def generate(size, maxValue):
    values = []
    for i in range(size):
        values.append(random.randint(1, maxValue))
    return values

