from tasks.data_stuctures.bracket_sequence.solution import is_correct_bracket_seq


def test_empty_string():
    # Пустая строка считается корректной
    assert is_correct_bracket_seq("") is True


def test_valid_sequences():
    assert is_correct_bracket_seq("()")
    assert is_correct_bracket_seq("{[()()]}")


def test_invalid_order():
    # Нарушен порядок закрытия
    assert not is_correct_bracket_seq("([)]")


def test_extra_closing_bracket():
    assert not is_correct_bracket_seq("())")


def test_long_sequence():
    # Проверка линейной сложности
    assert is_correct_bracket_seq("()" * 100_000)
