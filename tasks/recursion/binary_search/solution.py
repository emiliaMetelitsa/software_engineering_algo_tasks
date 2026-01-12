def binary_search(arr: list[int], target: int) -> int:
    """
    Возвращает индекс элемента или -1.
    """

    left, right = 0, len(arr) - 1

    while left <= right:
        # Используем середину текущего диапазона
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1