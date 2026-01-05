def is_correct_bracket_seq(s: str) -> bool:
    """
    Проверяет корректность скобочной последовательности.
    Используется стек, так как требуется LIFO-поведение.
    """

    stack = []

    # Отображение закрывающей скобки в соответствующую открывающую
    closing_to_opening = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for char in s:
        # Открывающие скобки просто кладём в стек
        if char in closing_to_opening.values():
            stack.append(char)
            continue

        # Если закрывающая — проверяем соответствие последней открывающей
        if not stack or stack.pop() != closing_to_opening[char]:
            return False

    # После обработки всей строки стек должен быть пуст
    return not stack