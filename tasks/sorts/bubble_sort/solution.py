def bubble_sort(arr: list[int]) -> list[list[int]]:
    """
    Пузырьковая сортировка.
    Возвращает снимки массива после каждого прохода с обменами.
    """

    data = arr[:]
    snapshots = []

    for i in range(len(data)):
        swapped = False

        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if swapped:
            snapshots.append(data[:])
        else:
            # Если обменов не было с самого начала — массив уже отсортирован
            if i == 0:
                snapshots.append(data[:])
            break

    return snapshots