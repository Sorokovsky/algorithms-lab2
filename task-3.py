from random import randint


def process_array(array: list) -> list:
    result = []
    sequence = []
    for i in range(len(array)):
        item = array[i]
        if item <= 0:
            if len(sequence) > 0:
                for item_in_sequence in sequence[::-1]:
                    result.append(item_in_sequence)
            sequence = []
            result.append(array[i])
        else:
            sequence.append(item)
    return result


def main():
    count = 100
    min = -50
    max = 50
    array = [randint(min, max) for _ in range(count)]
    print("Вхідний масив", array, sep=": ")
    print("Вихідний масив", process_array(array), sep=": ")


if __name__ == '__main__':
    main()
