from tasks.sorts.bubble_sort.solution import bubble_sort


def test_already_sorted():
    assert bubble_sort([1, 2, 3]) == [[1, 2, 3]]


def test_reverse_order():
    assert bubble_sort([3, 2, 1]) == [
        [2, 1, 3],
        [1, 2, 3]
    ]


def test_with_duplicates_and_negatives():
    assert bubble_sort([7, -2, -1]) == [
        [-2, -1, 7]
    ]


def test_multiple_passes():
    assert bubble_sort([3, 7, 9, 4, 3, 1, 8, 5]) == [
        [3, 7, 4, 3, 1, 8, 5, 9],
        [3, 4, 3, 1, 7, 5, 8, 9],
        [3, 3, 1, 4, 5, 7, 8, 9],
        [3, 1, 3, 4, 5, 7, 8, 9],
        [1, 3, 3, 4, 5, 7, 8, 9]
    ]


def test_large_list_complexity():
    arr = list(range(300, 0, -1))  # 300 элементов
    snaps = bubble_sort(arr)
    assert snaps[-1] == list(range(1, 301))
