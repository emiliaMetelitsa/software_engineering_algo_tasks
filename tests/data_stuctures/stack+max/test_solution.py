from tasks.data_stuctures.stack_max.solution import StackMax


def test_empty_stack():
    s = StackMax()
    assert s.get_max() == "None"
    assert s.pop() == "error"


def test_push_and_pop():
    s = StackMax()
    s.push(5)
    s.push(10)
    assert s.get_max() == 10
    s.pop()
    assert s.get_max() == 5


def test_negative_values():
    s = StackMax()
    s.push(-5)
    s.push(-2)
    assert s.get_max() == -2


def test_many_operations():
    s = StackMax()
    for i in range(10_000):
        s.push(i)
    assert s.get_max() == 9999
