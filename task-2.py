def first_matrix() -> list:
    width = 7
    height = 7
    result = []
    for row in range(height):
        row_array = []
        for column in range(width):
            if row % 2 == 1:
                row_array.append(0)
            else:
                row_array.append(1)
        result.append(row_array)

    return result


def second_matrix() -> list:
    width = 7
    height = 7
    result = []
    for row in range(height):
        row_array = []
        current = height - row
        need_decrees = False
        for column in range(width):
            if current == width:
                need_decrees = True
            row_array.append(current)
            if need_decrees:
                current -= 1
            else:
                current += 1
        result.append(row_array)
    return result


def print_matrix(matrix: list, name: str = "Матриця") -> None:
    print(f"Матриця: '{name}'")
    for row in matrix:
        for column in row:
            print(column, end=' ')
        print()


def main():
    print_matrix(first_matrix(), "Перша таблиця")
    print_matrix(second_matrix(), "Друга таблиця")


if __name__ == '__main__':
    main()
