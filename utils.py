import random


# Wysłanie menu z wyborem dla użytkownika
def menu(title, options):
    print("-----------")
    print(title)
    for index, option in enumerate(options):
        print(f'  [{index + 1}.] {option}')
    print("-----------")


# Generowanie losowego ciągu liczb
def generate(size):
    values = []
    for i in range(size):
        values.append(random.randint(1, size * 10))
    return values


def generate_increasing_sequence(size):
    return [random.randint(0, 10) + i*10 for i in range(size)]


def generate_decreasing_sequence(size):
    return [random.randint(0, 10) + i*10 for i in range(size)][::-1]


def generate_v_shaped_sequence(size):
    half = size // 2
    sequence = [random.randint(0, 10) + i*10 for i in range(half, 0, -1)]
    sequence.extend(random.randint(0, 10) + i*10 for i in range(1, half + 1))
    return sequence


def generate_a_shaped_sequence(size):
    half = size // 2
    sequence = [random.randint(0, 10) + i*10 for i in range(1, half + 1)]
    sequence.extend(random.randint(0, 10) + i*10 for i in range(half, 0, -1))
    return sequence
