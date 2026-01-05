from tasks.sorts.insertion_sort.solution import insertion_sort


def test_empty_and_single():
    assert insertion_sort([]) == []
    assert insertion_sort([5]) == [5]


def test_basic_unsorted():
    assert insertion_sort([9, 5, 1, 4, 3]) == [1, 3, 4, 5, 9]


def test_reverse_order():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_with_duplicates():
    assert insertion_sort([2, -1, 2, -1, 0]) == [-1, -1, 0, 2, 2]


def test_large_n_complexity():
    # проверка работы на 1000 элементов
    arr = list(range(1000, 0, -1))
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == list(range(1, 1001))
