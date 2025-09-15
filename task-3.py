from random import randint


def process_array(array: list) -> list:
    result = []
    temp = []
    has_sequence = False
    for i in array:
        result.append(i)
    for i in range(len(result)):
        if result[i] < 0 and has_sequence and len(temp) >= 2:
            index = i - len(temp)
            temp = temp[::-1]
            for j in range(len(temp)):
                result[index] = temp[j]
                index += 1
            temp = []
            has_sequence = False
        if result[i] >= 0:
            temp.append(result[i])
            has_sequence = True
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
