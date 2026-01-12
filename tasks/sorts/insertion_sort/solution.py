def insertion_sort(arr: list[int]) -> list[int]:
    """
    Сортировка вставками.

    """

    result = arr[:]

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        # Сдвигаем элементы вправо, пока не найдём позицию
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result