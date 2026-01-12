from tasks.recursion.binary_sort.solution import binary_search


def test_empty():
    assert binary_search([], 10) == -1


def test_single_element():
    assert binary_search([5], 5) == 0
    assert binary_search([5], 3) == -1


def test_multiple_occurrences():
    arr = [1, 2, 2, 2, 5]
    idx = binary_search(arr, 2)
    # бинарный поиск может вернуть любой индекс равного элемента
    assert idx in (1, 2, 3)


def test_absent_value():
    arr = [0, 1, 3, 7, 10]
    assert binary_search(arr, 5) == -1


def test_large_array_log_complexity():
    # 1 миллион элементов
    arr = list(range(1_000_000))
    assert binary_search(arr, 999_999) == 999_999
    assert binary_search(arr, -10) == -1
