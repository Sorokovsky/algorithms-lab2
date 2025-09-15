def enter_array() -> list:
    try:
        count = int(input("Введіть довжину масиву: "))
        if count < 0:
            print("Число має бути більше рівне 0")
            return enter_array()
        array = []
        for i in range(count):
            array.append(int(input(f"Введіть число під індексом {i}: ")))
        return array
    except ValueError:
        print("було введено не число.")
        return enter_array()


def process_array(array: list) -> list:
    min = None
    max = None
    result = []
    for item in array:
        result.append(item)
        if item < 0:
            if max is None:
                max = item
            elif item > max:
                max = item
        else:
            if min is None:
                min = item
            elif item < min:
                min = item
    if max is not None:
        result.insert(0, max)
    if min is not None:
        result.insert(len(result), min)
    return result


def main():
    array = enter_array()
    print(array)
    array = process_array(array)
    print(array)


if __name__ == "__main__":
    main()
